---
title: Epee/ZMQ Serialization Future
source_url: https://github.com/monero-project/monero/issues/6406
author: vtnerd
assignees: []
labels: []
created_at: '2020-03-27T23:08:47+00:00'
updated_at: '2020-03-27T23:09:36+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I've analyzed the serialization code in epee (p2p, http), cryptonote (internal db), and zmq. The problems I've identified:

Immediate EDIT: "Problems" might be the wrong word. Performance limiting stuff? It does work after all.

- ZMQ only supports JSON
  - Binary data has to be converted to/from hex which is slower and increases the payload size 
  - The hex conversion is a definite hot-spot when profilng (Monero uses _lots_ of binary data in its RPC for cryptographic data).
- ZMQ serialization requires specifying the field names twice - for both reading and writing (unlike epee stuff).
- Epee uses a DOM internally when reading/writing.
  - _At least_ as slow (not actually clocked) as rapidjson DOM code due to its more generic `std::map<std::string, variant<...>>` design.
  - Removing the rapidjson DOM from zmq-json output had a ~33% performance gain.
- Epee currently has everything in header (via templates), which increases compile times.

After (too?) many iterations - the solution below should support JSON, epee binary, or msgpack binary, and can be used by the ZMQ, P2P, and HTTP components. The ZMQ will be the easiest to retrofit, and the other components (P2P, HTTP) can be done optionally.  The code CAN support reading without a DOM, but the simpler (intermediate DOM) implementation was used here for reading (writing uses no DOM).

This uses `BOOST_PP` AND C++11 variadics. So its a double-shot of fun, but actually less total code than epee or cryptonote schemes (but far more dense).

I'm primarily sharing this to start a discussion on whether its worth doing the remaining integration (I had versions of this working with ZMQ actually, but needs some cleanup). Also, it might be worth preserving this effort for ideas.

The usage looks like:
```c++
// multiple types could be supported with different macro names.
// header
WIRE_JSON_DECLARE(cryptonote::transaction);
WIRE_JSON_DECLARE(cryptonote::tx_out);
// cpp
WIRE_JSON_DEFINE(
  cryptonote::transaction, (
    version,
    unlock_time,
    WIRE_KV_N(vin, "inputs"),
    WIRE_KV_N(vout, "outputs"),
    extra,
    signatures,
    WIRE_KV_N(rct_signatures, "ringct")
  )
);

namespace
{
  template<typename F, typename T>
  void map_txout(F& format, T& self)
  {
    wire::object(format,
      MONERO_FIELD(amount),
      wire::variant_field(self.target,
        wire::option<txout_to_key>{"to_key"},
        wire::option<txout_to_script>{"to_script"},
        wire::option<txout_to_scripthash>{"to_scripthash"}
      )
    );
  }
}
WIRE_JSON_USE_MAP(tx_out, map_txout);
```
Perhaps the not so fun code making that happen:

```c++
// base header

//! Specify a JSON key for C/C++ member.
#define WIRE_FIELD_KEY(name, key)                \
  ::wire::field( key , std::ref( self . name ) )

//! Use `name` for C/C++ struct member and JSON key.
#define WIRE_FIELD(name)                         \
  WIRE_FIELD_KEY(name, BOOST_PP_STRINGIZE(name))

/*! Expand arguments into macro; needed due to preprocessor limitation.
    \param func macro to expand
    \param ... arguments for `func`. */
#define WIRE_FIELD_INVOKE(func, ...) \
  func (__VA_ARGS__)

//! \param args Boost preprocessor tuple where FRONT is macro to expand and TAIL are arguments to that macro.
#define WIRE_FIELD_UNPACK(args)                                                                        \
  WIRE_FIELD_INVOKE(BOOST_PP_TUPLE_ELEM(0, args), BOOST_PP_TUPLE_ENUM(BOOST_PP_TUPLE_POP_FRONT(args)))

//! Specify explicit key name in fields tuple; expanded by `MONERO_FIELD_UNPACK`.
#define WIRE_KV_N(name, key)  \
  (WIRE_FIELD_KEY, name, key)

/*! For use by `BOOST_PP_SEQ_FOR_EACH_I`. Prefixes a comma when `index != 0` and
    then expands `args` for field.
 
    \param index The position the field will be stored. In the future this may
      be used for message pack integer keys. Also used for optional comma
      prefix.
    \param args A single token given to `MONERO_FIELD` OR a Boost preprocessor
      tuple given to `MONERO_FIELD_UNPACK`. */
#define WIRE_FIELD_EXPAND(z, _, index, args)                                                                \
  BOOST_PP_COMMA_IF(index) BOOST_PP_IF(BOOST_PP_IS_BEGIN_PARENS(args), WIRE_FIELD_UNPACK, WIRE_FIELD)(args)

/*! Define an inline function `name` that expands a tuple of `fields` so that a
    C/C++ struct can be translated to key/value pairs. The supported key types
    are integers or strings. The function calls `serialize_object` with the
    expanded list of fields.

    \note Listing all fields in a single C++11 variadic function has the
      advantage of allowing for unordered field formats (JSON, msgpack, etc.) to
      be read into C/C++ structs without creating an intermediate DOM/map. The
      existing epee macro system doesn't allow for this, because the parser
      doesn't know the entire list of valid keys.

    \param name A valid C++ function name.
    \param A Boost preprocessor "tuple" of fields, where each field is either a
      single token representing the C/C++ struct member name and JSON key OR a
      Boost processor tuple that gets expanded later (`MONERO_FIELD_UNPACK`).
      Use `MONERO_KV_` macros if default `MONERO_FIELD` expansion is insufficient.

    \example `MONERO_FIELD_MAP(transaction, (extra, MONERO_KV_N(vout, "outputs"), signatures))` */
#define WIRE_FIELD_MAP(name, fields)                                               \
  template<typename F, typename T>                                                 \
  inline void name (F&& format, T&& self)                                          \
  {                                                                                \
    ::wire::object(                                                                \
      std::forward<F>(format),                                                     \
      BOOST_PP_SEQ_FOR_EACH_I(WIRE_FIELD_EXPAND, _, BOOST_PP_TUPLE_TO_SEQ(fields)) \
    );                                                                             \
  }

namespace wire
{
  template<typename T>
  struct unwrap_reference
  {
    using type = T;
  };

  template<typename T>
  struct unwrap_reference<std::reference_wrapper<T>>
  {
    using type = T;
  };


  //! Links `name` to a `value` for object serialization.
  template<typename T>
  struct field_
  {
    using value_type = typename unwrap_reference<T>::type;

    char const* const name;
    T value;

    //! \return `value` with `std::reference_wrapper` removed.
    constexpr const value_type& get_value() const
    {
      return value;
    }

    //! \return `value` with `std::reference_wrapper` removed.
    value_type& get_value()
    {
      return value;
    }
  };

  //! Links `name` to `value`. Use `std::ref` if de-serializing.
  template<typename T>
  constexpr inline field_<T> field(const char* name, T value)
  {
    return {name, std::move(value)};
  } 


  //! Links a variant type to a string name/key.
  template<typename T>
  struct option
  {
    char const* const name;
  };

  //! Get the name for `T` from a `variant_field_`. Compilation error means missing type.
  template<typename T, typename U>
  constexpr const char* get_option_name(const U& field) noexcept
  {
    return static_cast< const option<T>& >(field).name;
  }

  //! Links each type in a variant to a string key.
  template<typename T, typename... U>
  struct variant_field_ : option<U>...
  {
    using value_type = typename unwrap_reference<T>::type;

    constexpr variant_field_(T value, option<U>... opts)
      : option<U>(opts)..., value(std::move(value))
    {}

    T value; //!< Must be a variant-compatible type

    //! \return `value` with `std::reference_wrapper` removed.
    constexpr const value_type& get_value() const
    {
      return value;
    }

    //! \return `value` with `std::reference_wrapper` removed.
    value_type& get_value()
    {
      return value;
    }

    //! Wraps visitor so that the name associated with the type can be retrieved
    template<typename V>
    struct wrap
    {
      using result_type = void;

      variant_field_ self;
      V visitor;

      template<typename X>
      void operator()(const X& value) const
      {
        visitor(::wire::get_option_name<X>(self), value);
      }
    };

    /*! Provide `visitor` with active variant value. 
        \tparam V callable with signature `void(const char*, T)` for each `U`
          type. The string is the key associated with the type. */
    template<typename V>
    void visit(V visitor) const
    {
      // found via ADL - `value_type` must be a variant with an associated `apply_visitor` function
      apply_visitor(wrap<V>{*this, std::move(visitor)}, get_value());
    }
  };

  //! Links variant `value` to a unique name per type in `opts`. Use `std::ref` for `value` if de-serializing.
  template<typename T, typename... U>
  constexpr inline variant_field_<T, U...> variant_field(T value, option<U>... opts)
  {
    return {std::move(value), opts...};
  }
} // wire

// json header

/*! Defines `write_json` and `read_json` for `type` that uses function
    `map_name` to translate between C/C++ members and JSON keys.

    \param type A valid C++ struct.
    \param map_name A previously defined "mapping" function. See
      `MONERO_FIELD_MAP` for expected function signature and behavior. */
#define WIRE_JSON_USE_MAP(type, map_name)                                              \
  void read_json(const rapidjson::Value& src, type & dest)                         \
  {                                                                                    \
    map_name (src, dest);                                                              \
  }                                                                                    \
  void write_json(rapidjson::Writer<rapidjson::StringBuffer>& dest, const type & src) \
  {                                                                                    \
    map_name (dest, src);                                                              \
  }

/*! Defines `write_json` and `fromJsonVaue` for `type` in the current
    namespace, and a defines a mapping function called `map_name` in an
    anonymous namespace (within the current namespace).

    \param type A C/C++ struct.
    \param map_name A valid C++ function name.
    \param fields See `MONERO_FIELD_MAP`. */
#define WIRE_JSON_DEFINE_NAMED(type, map_name, fields)   \
  namespace                                              \
  {                                                      \
    WIRE_FIELD_MAP(map_name, fields)                     \
  }                                                      \
  WIRE_JSON_USE_MAP(type, map_name)

/*! Define `write_json` and `read_json` in current namespace, that map
    `fields` to `type`. Each usage of this function must be on its own line.

    \param type A C/C++ struct.
    \param fields See `MONERO_FIELD_MAP`. */
#define WIRE_JSON_DEFINE(type, fields)                                     \
  WIRE_JSON_DEFINE_NAMED(type, BOOST_PP_CAT(field_map_, __LINE__), fields)

namespace wire
{
  namespace json
  {
    template<typename T, typename U>
    bool read_option(const rapidjson::Value& src, U& dest, const char* name)
    {
      auto member = src.FindMember(name);
      if (member != src.MemberEnd())
        return false;
      
      T value{};
      read_json(src, value);
      dest = std::move(value);
      return true;
    }

    struct write_option
    {
      rapidjson::Writer<rapidjson::StringBuffer>& dest;

      template<typename T>
      void operator()(const char* name, const T& value) const
      {
        dest.Key(name);
        write_json(dest, value);
      }
    };
    
    template<typename T>
    bool read_field(const rapidjson::Value& src, field_<T> dest)
    {
      auto member = src.FindMember(dest.name);
      if (member == src.MemberEnd())
        throw json::MISSING_KEY{dest.name};

      read_json(member->value, dest.get_value());
      return true;
    }

    template<typename T, typename... U>
    bool read_field(const rapidjson::Value& src, variant_field_<T, U...> dest)
    {
      const bool available[] = {read_option<U>(src, dest.get_value(), ::wire::get_option_name<U>(dest))...};
      if (std::count(std::begin(available), std::end(available), std::size_t(0)) != 1)
        throw MISSING_KEY{"expected one key for variant"};
      return true;
    }

    template<typename T>
    bool write_field(rapidjson::Writer<rapidjson::StringBuffer>& dest, const field_<T> src)
    {
      dest.Key(src.name);
      write_json(dest, src.get_value());
      return true;
    }

    template<typename T, typename... U>
    bool write_field(rapidjson::Writer<rapidjson::StringBuffer>& dest, const variant_field_<T, U...> src)
    {
      src.visit(json::write_option{dest});
      return true;
    }
  } // json

  //! Reads `fields...` from `src`.
  template<typename... T>
  void object(const rapidjson::Value& src, const T... fields)
  {
    if (!src.IsObject())
      throw json::wrong_type{"json object"};
    const bool dummy[] = {json::read_field(src, fields)...};
  }

  //! Writes `fields...` to `dest`.
  template<typename... T>
  void object(rapidjson::Writer<rapidjson::StringBuffer>& dest, const T... fields)
  {
    dest.StartObject();
    const bool dummy[] = {json::write_field(dest, fields)...};
    dest.EndObject(sizeof...(T));
  }
} // wire
```

# Discussion History
# Action History
- Created by: vtnerd | 2020-03-27T23:08:47+00:00
