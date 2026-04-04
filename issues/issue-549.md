---
title: Matrix.monero.social Matrix Instance Issues + General Tasklist
source_url: https://github.com/monero-project/meta/issues/549
author: scottAnselmo
assignees: []
labels: []
created_at: '2021-02-07T22:12:34+00:00'
updated_at: '2021-09-30T07:02:18+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Comment any other found Issues or suggested tasks and I'll update accordingly.

### Issues

- [x]  **Problem:** Tutanota blocking registration emails, ProtonMail is sending to spam

**Root Cause:** Likely emails are rated high for spamyness; confirm and address using a service like https://www.mail-tester.com/ Will require either rehrar or pigeons to address improvements to make on email server

- [x] **Problem:** Can't add matrix.monero.social as a searchable room when on other home servers

![image](https://user-images.githubusercontent.com/3056597/107160746-0aa93300-6990-11eb-9560-b8da7dff1e0d.png)
**Root Cause:** Synapse config may not be set to make rooms publicly discoverable



### General Tasklist

- [ ] **Task:** Create Matrix rooms on Matrix.monero.social and bridge with freenode channels. (Optional) Ideally convince users on Matrix.org to leave Matrix.org rooms and move to monero.social rooms so Matrix.org rooms can be decommissioned. @erciccione has proposed a series of steps for the user migration from Matrix.org room to monero.social room:

1. Ask admins of the rooms which should be migrated if they are willing to make the room inaccessible and "migrate" to the new server.
2. If they agree, create the public room
3. Ping all people in the old room (@room) and invite them to join the new room
4. Change the description of the room to let people know it has been migrated
5. Kick everybody out from the old room (can be done using API)
6. Make old room inaccessible
7. Make sure the new room is published and available from other servers 

**Requirements:** Someone with ops on the IRC channel to quickly accept the bridge request; persons may vary by channel

Referenced on getmonero.org (updated bridge state 2020/02/11):

- [x] #monero

- [x] #monero-markets

- [x] #monero-pools

- [ ] #monero-hardware 

- [x] #monero-community

- [ ] #monero-offtopic

- [ ] #monero-research-lab

- [x] #monero-site

- [x] #monero-dev

- [ ] #monero-otc

- [ ] #monero-translations

Other:

- [ ] #monero-defcon



- [ ] **Task:** Create what's known as a 'Community' in Matrix, AKA a set of rooms. Should be done after all Issues are addressed and rooms are bridged to all website listed channels

- [ ] **Task:** Update getmonero.org IRC page's Matrix links to point to monero.social rooms after the rooms have been bridged with their IRC counterparts

- [ ] **Task:** Make sure E2EE is enabled by default for non public rooms (encryption_enabled_by_default_for_room_type: invite). _This can only be done by an admin (rehrar or pigeons)_

- [ ] **Task:** If the members of the core team don't want to register an account, make their nick unavailable to be registered (can be done through the homeserver.yaml file). This will avoid impersonation problems (at least for the monero.social homeserver). _This can only be done by an admin (rehrar or pigeons)_


# Discussion History
## erciccione | 2021-02-08T10:34:06+00:00
> Problem: Can't add matrix.monero.social as a searchable room when on other home servers

As far as i know the address is `monero.social`, not `matrix.monero.social`. Federation seems to be set up correctly (https://federationtester.matrix.org/#monero.social), but yes, probably some settings need to be tweaked.

> Create Matrix rooms on Matrix.monero.social and bridge with freenode channels. Ideally convince users on Matrix.org to leave Matrix.org rooms and move to monero.social rooms so Matrix.org rooms can be decommissioned

This could be a problem. There isn't an option to remove rooms, which means that to make a room inaccessible all users in the room must leave (or be kicked). Admins can make the room inaccessible in other ways, but not remove it.

Probably this is the best way to proceed:

1. Ask admins of the rooms which should be migrated if they are willing to make the room inaccessible and "migrate" to the new server.
1. If they agree, create the public room
2. Ping all people in the old room (`@room`) and  invite them to join the new room
3. Change the description of the room to let people know it has been migrated
4. Kick everybody out from the old room (can be done using API)
5. Make old room inaccessible
6. Make sure the new room is published and available from other servers

Alternatively, it's possible to leave the rooms on the matrix homeserver and instead alias them on the monero.social server. This is the least problematic and trouble-free option, but probably the less liked.

Consider that some admins might be not willing to migrate their rooms. I, for example, i have at least one room (Monero Website), which was not created on the matrix homeserver, but on my own. There is no reason to migrate this room, but i will definitely alias it to an address on `monero.social`. That will cause Monero's server to be used as a backup in the case my homeserver goes down. Makes also easier to find the new rooms.

> Task: Create what's known as a 'Community' in Matrix, AKA a set of rooms. Should be done after all Issues are addressed and rooms are bridged to all website listed channels

Note that 'communities' on matrix have very limited reason to exist at the moment. I created the 'monero' community on matrix and found it useful only to have a directory of rooms and to show the shiny Monero flair in other communities.

> Task: Update getmonero.org IRC page's Matrix links to point to monero.social rooms after the rooms have been bridged with their IRC counterparts

Just ping me or open an issue on monero-site when it's time to get to this.

I have more tasks to propose:

- [ ] make sure E2EE is enabled by default for non public rooms (`encryption_enabled_by_default_for_room_type: invite`)
- [ ] If the members of the core team don't want to register an account, make their nick unavailable to be registered (can be done through the `homeserver.yaml` file). This will avoid impersonation problems (at least for the monero.social homeserver)

Side note: if people want to migrate their matrix.org account to a newly created monero.social account, they can use https://ems.element.io/tools/matrix-migrati

## erciccione | 2021-02-09T11:56:08+00:00
I'm taking a look at the monero.social homeserver and i'm noticing the Monero rooms were already created and bridged to freenode. This is not an optimal approach and will create confusion. Also, users already created a monero.social matrix account and are posting on the newly created rooms. Matrix users on monero.social and matrix.org cannot communicate and are exchanging messages through the freenode bridge. This is unnecessary load for the matrix freenode bridge and any other homeserver currently connected to these rooms.

Furthermore, creating these rooms so early without removing the old ones will make much harder (if not impossible) to alias the new rooms to the old address. As a result there will always be two Monero rooms: the one on matrix.org and the one on monero.social. One can be made inaccessible, but could still be source of confusion.

One more task:

- [ ] Freenode users in the matrix rooms don't have the appropriate flair (+freenode:matrix.org). The flair can be set directly in the room, but IIRC there is also an option in the synapse configuration file.

## SamsungGalaxyPlayer | 2021-02-09T13:55:44+00:00
Why would we want to remove the matrix.org rooms? Isn't it for our benefit that these rooms show up in the main room lists on matrix.org? Or would users be able to easily see the monero.social rooms in the same public matrix.org list without changing servers?

## erciccione | 2021-02-09T14:48:00+00:00
> Why would we want to remove the matrix.org rooms?

Having two 'same' rooms on two different servers is not expected behaviour and creates problems. As i mentioned above, matrix users on two different servers are not interacting directly as they should, but they are passing through the Freenode bridge:

```
#monero:matrix.org <-> freenode bridge <-> freenode <-> freenode bridge <->  #monero:monero.social
```

That's why matrix users who are using the monero.social room are seen as freenode users in the matrix.org room.

This structure also makes moderation problematic. For example users banned on one room won't be banned on the other an all settings should be always changed twice.

The correct behaviour should be

```
#monero:monero.social (ideally) aliased to #monero:matrix.org <-> freenode bridge <-> freenode
```

I say 'ideally' because to manage to do that, we should go throught the steps i described in https://github.com/monero-project/meta/issues/549#issuecomment-775045232, which is not easy.

Excluding the option above, the best solution would have probably been to alias the `#monero-*:matrix.org` rooms to `#monero-*:monero.social `and make the latter the primary address. Now that the rooms have been created i'm not sure if this would work, since the name is already taken and deleting rooms is not as easy as one might expect.

> Or would users be able to easily see the monero.social rooms in the same public matrix.org list without changing servers?

Yes, changing servers is not necessary. monero.social rooms can be published to other servers by having a user of these servers with admin powers on the monero.social rooms check the option  `Publish this room to the public in matrix.org room directory?
` in the settings.

## subiol | 2021-02-09T17:52:28+00:00
Hi

I am the admin of Monero-markets. I was trying to create the room in monero.social. In matrix.org the room has two aliases moneromarkets:matrix.org and monero-markets:matrix.org. I have been able to add the moneromarkets:monero.social to the room, but when I have tried to add monero-markets:monero.social it gave me an error, because that address is already in use.

I am not sure how viable is to delete the room so I can add the address to the existing room, but I will follow this issue so we can solve it. Feel free to ping me if you need any action from me.

## SamsungGalaxyPlayer | 2021-02-09T18:05:10+00:00
@subiol I added the relay for #monero-markets. I can add you as admin there and leave if you confirm by DM to me on Freenode (sgp_)

## subiol | 2021-02-09T18:13:46+00:00
@SamsungGalaxyPlayer I am not sure that would solve the issue because there would still be two rooms. Maybe @erciccione can confirm this I'm saying is correct. What I think needs to happen is for the current #monero-markets:monero.social room to be deleted, so I can add the address to the old room.

If you check the rooms available in monero.social right now you will see there is two monero markets rooms, moneromarkets:monero.social and monero-markets:monero.social.

With the relay you mean a bridge to freenode irc? Right now the monero markets room is bridged to irc with the relay on matrix.org, but i have no problem stopping that one and using the relay at monero.social if you guys prefer it that way.

## scottAnselmo | 2021-02-12T05:30:54+00:00
Added @erciccione's suggested tasks, updated bridge status.

Side note, the URL provided for user semi-automated migration of home servers kicked off by a user was cutoff, the working URL is: https://ems.element.io/tools/matrix-migration

## erciccione | 2021-02-12T10:09:10+00:00
> If the members of the core team don't want to register an account, make their nick unavailable to be registered 

This is a security risk and should be fixed as soon as possible. Registrations are already open.

> Create what's known as a 'Community' in Matrix,

Community will be soon replaced by "Spaces"(unclear what these 'spaces' will be for now) .So, i wpould remove this task.

>  #monero-site

Why and how was this bridged? The room has already a monero.social address. Where is the bridge working on? That would explain why some matrix users are starting to showing up as freenode users.

**Please do not relay any other room**. As i explained above the current configuration is wrong and more rooms will be bridged more confusion and more load for the freenode bridge (which is being already overloaded) will be the result.

## subiol | 2021-02-12T10:18:28+00:00
I spoke with the guys at the Matrix channel and I think I found the best solution for the duplicated channels.

The new duplicated rooms should be tombstone'd. When you emit a tombstone event on a room, that room is prevented from receiving new messages (nobody can speak anymore) and it can point to another room. If another room is indicated in the tombstone event, the users in that room will see a button in their chat bar that, when pressed, will automatically make them join the other room and abandon the tombstone'd room. It switches one room for the other without the user having to do anything but click a button to confirm the action.

So basically, we should tombstone the new duplicated rooms (change their address first so it can be taken by the old room) pointing to the old rooms. That way the users of the new duplicated room only have to press the button and join everybody.

## scottAnselmo | 2021-02-12T16:45:23+00:00
> Why and how was this bridged? The room has already a monero.social address. Where is the bridge working on?

My understanding is that because it's showing up on monero.social, the bridge was monero.social <-> haveno.network <-> freenode, not monero.social to freenode directly? But perhaps I'm misreading the UI here and should uncheck it?

![image](https://user-images.githubusercontent.com/3056597/107796337-a2709d80-6d51-11eb-8aa9-f7fe6f69e856.png)


## scottAnselmo | 2021-02-16T15:36:56+00:00
Updated both Tutanota not getting emails and addability of monero.social for room search as both are fixed post downtime yesterday.

## sethforprivacy | 2021-02-16T15:54:26+00:00
It appears that usernames on monero.social are bugged or broken due to the Freenode double proxy:

![matrix](https://user-images.githubusercontent.com/40500387/108087324-3baff480-706f-11eb-996e-8c919ca02ac2.png)


## SamsungGalaxyPlayer | 2021-02-16T16:02:25+00:00
User guides tasks:

* [x] Web: https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web
* [ ] Desktop: TBD (lowest priority imo)
* [x] Android: https://forum.monero.space/d/81-how-to-join-the-monero-core-team-matrix-server-android
* [ ] iOS: TBD

Guide requirements:

* [ ] Make user account
* [ ] Join a room with that account
* [ ] Login with an existing user account

## erciccione | 2021-02-16T22:41:02+00:00
> It appears that usernames on monero.social are bugged or broken due to the Freenode double proxy:

~~I have the feeling the source of this problem is not getting the attention it should get. The way rooms were created and relayed is broken and should be fixed as soon as possible. It will get worse with time and with more people joining the two different rooms and with more load added to the freenode bridge maintained by matrix. This should have the priority on everything else.~~

Edit: Just talking about it. The problems should be solved and the rooms are being relayed.

## SamsungGalaxyPlayer | 2021-02-17T00:04:07+00:00
Room Bridge Progress (will update)



Freenode   Channel | matrix.org | monero.social | matrix.org <>   monero.social | Working Matrix<>IRC Relay | Working Discord<>IRC Relay
-- | -- | -- | -- | -- | --
#monero | #monero |  | ***No*** | Matrix.org | #monero
#monero-community | #monero-community | #monero-community | Yes | Matrix.org | #monero-community
#monero-space | #monero-space | #monero-space | Yes | Matrix.org | #monero-space
#monero-dev | #monero-dev | #monero-dev | Yes | Matrix.org | #monero-dev
#monero-offtopic | #monero-offtopic | #monero-offtopic | Yes | Matrix.org | No
#monero-markets | #monero-markets | #monero-markets | Yes | Matrix.org | #monero-markets
#monero-pools | #monero-pools | #monero-pools | Yes | Matrix.org | #monero-pools
#monero-memes | #monero-memes | #monero-memes | Yes | Matrix.org | #monero-memes
#monero-research-lab | #monero-research-lab | #monero-research-lab | Yes | Matrix.org | #monero-researchlab
#monero-research-lounge | #monero-research-lounge | #monero-research-lounge | Yes | Matrix.org | No
#monero-pt | #monero-pt |  #monero-pt | Yes | Matrix.org | No
Russian room (?) |   |   |   |   | No
#monero-gui | #monero-gui | #monero-gui | Yes | ***No*** | No
#monero-pow | #monero-pow | #monero-pow | Yes | ***No*** | No
#monero-otc |   |   |   |   | #monero-otc
#monero-site | #monero-website | #monero-site  | Yes | Matrix.org | No
#monero-translations | #monero-localizations | #monero-translations | Yes | Matrix.org | No
#monero-support | #monero-support | #monero-support | Yes | Matrix.org | No
#monero-policy | #monero-policy | #monero-policy | Yes | Matrix.org | No

## subiol | 2021-02-17T01:36:05+00:00
Not trying to add more work, but as I commented to spg in communities, it would be cool if monero.social could run the matrix-discord bridge, and obviously turn off the irc-discord bridge. The advantage would be each discord member having its own user (just like the irc-matrix bridge does) as opposed to now where the discord users all write under the same user.

This is the github of the matrix-discord bridge, with all the instructions on how to run it: https://github.com/Half-Shot/matrix-appservice-discord . It is maintained by half-shot which is the same guy maintaining the irc-matrix bridge and in my experience is responsive to any doubts.

## SamsungGalaxyPlayer | 2021-02-17T02:53:27+00:00
@subiol the Discord relay is in the Monero Space wheelhouse. Please discuss in #monero-space and/or make a post in forum.monero.space. It's a good idea.

## erciccione | 2021-02-17T08:31:02+00:00
> #monero-site

Already has a monero.social address: `#monero-site:monero.social`

> #monero-translations

Now has a `:monero.social` address: `#monero-translations:monero.social`

## erciccione | 2021-02-17T08:57:29+00:00
- [ ] The freenode rooms on matrix which have a native matrix room should be made invisible.

![Screenshot from 2021-02-17 08-53-29](https://user-images.githubusercontent.com/28106476/108179297-5cbf2680-70fd-11eb-8548-80dc9984f2ce.png)

As you can see from the screenshot above the freenode bridge is publicly accessible. This is reduntant and confusing, because people from matrix should always join the matrix rooms. These bridge-rooms should be made not accessible by a mod/admin.

Instructions:

1. Join the freenode room (in the example in the screneshot would be: `#freenode_#monero:matrix.org`) with a `matrix.org` user with mod powers
2. Deselect the option "publish this room to the public in matrix.org"
3. If the bridges are public on other servers (like `monero.social`), the room should be made invisible on that server as well (same procedure 1+2)


## subiol | 2021-02-17T09:04:50+00:00
Removing those bridges visibility is the minimum. Ideally those bridges should be shut down and the users redirected to join the equivalent matrix room that are bridged with IRC, but I doubt there is a way to do this.

I'll ask in the IRC matrix bridge room, but I'm not sure there will be a better solution than just remove the visibility.

## subiol | 2021-02-17T09:57:52+00:00
I was told in the IRC matrix bridge channel that to remove visibility or close the channel you need someone with more rank than appservice-irc:matrix.org, and because that channel was created directly by it, nobody has higher rank. So only option is to ask the owners of the bot to close that channel.

I am waiting for them to see my message in the chatroom. If they do not answer there, I have been recommended to open an issue on github.

If anyone knows any more of this type of channels that need to be closed, this would be the moment to speak so we can ask to close them all together.

EDIT: There are a lot of this type of rooms. If you do a search for '#freenode_#monero' you will see that there are around 20, some with an equivalent matrix room some not. Not sure if we should ask for the ones that have equivalent matrix room to be shut down, all or what.

## SamsungGalaxyPlayer | 2021-02-17T18:13:11+00:00
> Not sure if we should ask for the ones that have equivalent matrix room to be shut down, all or what.

Yes, shutting down all of these with a tombstone is ideal imo.

## subiol | 2021-02-17T18:54:13+00:00
> Yes, shutting down all of these with a tombstone is ideal imo.

No, these rooms are not real Matrix rooms, I am not sure what they are. But when the bot shuts them down they will just disappear. They can not be tombstone'd.

That is why I am asking which ones should we ask to be shut down, the ones that have a equivalent Matrix room, all of them or we decide case by case?

## SamsungGalaxyPlayer | 2021-02-17T19:41:55+00:00
@subiol in that case, all rooms matching the same relayed matrix room should be taken down imo. All of them in this list that are set up:

https://github.com/monero-project/meta/issues/549#issuecomment-780197739

## subiol | 2021-02-20T14:26:53+00:00
Did anyone ask already for the duplicated bridged rooms to be closed?

Since I got no response from me asking for the duplicated bridged rooms to be closed in the Matrix IRC bridge room, I was going to open an issue on its github page. But when I have gone to search for the duplicated rooms that need to be closed, most of them are already gone (only one duplicated left #freenode_#monero-space:matrix.org and there were a bunch more two days ago). I am not sure if they went and removed them without answering me on the room or someone else contacted them through another channel.

In any case, most of them are gone, only one is left, which I am going to ask in the chat to remove too, so this issue should be solved soon.

## erciccione | 2021-03-05T13:14:21+00:00
What's happening to #monero room? looks like it was broken for some time and a lot of matrix users inside got kicked out. i managed to join the room again, but other users are saying they cannot.

## subiol | 2021-03-06T08:34:42+00:00
> What's happening to #monero room? looks like it was broken for some time and a lot of matrix users inside got kicked out. i managed to join the room again, but other users are saying they cannot.

Yes, I tried to help a user that was in this situation. I asked on the matrix channel, and they told me the best way to find out what is happening is to check the logs of the server the user is using to log into matrix, as the log of the server should explain what the issue is.

The second thing they recommended is to check if the room has a server banned, as it can be done to avoid spam, but I highly doubt this is the issue.

As a final solution, the room could be tombstone'd and pointed to a newly created room that (hopefully) does not have this issues.

## garlicgambit | 2021-07-13T17:45:10+00:00
Suggest to make the server available as a Tor .onion service.  
  
This [issue](https://github.com/matrix-org/synapse/issues/5152) may be relevant.

## bclermont | 2021-09-30T07:02:17+00:00
as https://github.com/matrix-org/synapse/pull/10475 is merged, it should be possible now

# Action History
- Created by: scottAnselmo | 2021-02-07T22:12:34+00:00
