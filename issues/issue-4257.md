---
title: Incorrect getting block height from date
source_url: https://github.com/monero-project/monero-gui/issues/4257
author: developergames2d
assignees: []
labels: []
created_at: '2023-12-24T23:00:24+00:00'
updated_at: '2023-12-25T02:10:15+00:00'
type: issue
status: closed
closed_at: '2023-12-25T00:30:45+00:00'
---

# Original Description
I restored my wallet from date 2023-12-01, but monero-gui sets height ~1'500'000, while real height is ~3'032'307.
I used formula:
1'009'827 + get_difference_days(2016.03.23, 2023.12.01) * 720.

When I try to restore from height 3030000 (Mainnet), all is OK.

# Discussion History
## selsta | 2023-12-25T00:30:45+00:00
I don't know where you got this formula, it doesn't work. I linked you the correct formula here: https://github.com/monero-project/monero-gui/blob/master/js/Wizard.js#L134

Putting in the date 2023-12-01 gets the correct restore height.
```
console.log(getApproximateBlockchainHeight(new Date('Dec 01 2023'), "Mainnet"));
> 3010228
```

## developergames2d | 2023-12-25T02:02:19+00:00
> I don't know where you got this formula, it doesn't work. I linked you the correct formula here: https://github.com/monero-project/monero-gui/blob/master/js/Wizard.js#L134
> 
> Putting in the date 2023-12-01 gets the correct restore height.
> 
> ```
> console.log(getApproximateBlockchainHeight(new Date('Dec 01 2023'), "Mainnet"));
> > 3010228
> ```

I used this formula. But monero-gui sets ~1500000. Because of this, the synchronization is very long.

## selsta | 2023-12-25T02:04:44+00:00
<img width="1026" alt="gui1" src="https://github.com/monero-project/monero-gui/assets/7697454/4f7fa84b-2442-4920-96e5-d0593cfe6d06">
<img width="1026" alt="gui2" src="https://github.com/monero-project/monero-gui/assets/7697454/c0d1db9f-f63d-4063-8c82-3cb172e0518f">

Works without issues here, I entered `2023-12-01` and it set the restore height to `3010228`. Please make a screenshot how it looks for you.

## developergames2d | 2023-12-25T02:10:14+00:00
> <img alt="gui1" width="1026" src="https://private-user-images.githubusercontent.com/7697454/292698573-4f7fa84b-2442-4920-96e5-d0593cfe6d06.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDM0NzAxODYsIm5iZiI6MTcwMzQ2OTg4NiwicGF0aCI6Ii83Njk3NDU0LzI5MjY5ODU3My00ZjdmYTg0Yi0yNDQyLTQ5MjAtOTZlNS1kMDU5M2NmZTZkMDYucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQUlXTkpZQVg0Q1NWRUg1M0ElMkYyMDIzMTIyNSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyMzEyMjVUMDIwNDQ2WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YjliY2IyYTUzOWRmNzcyNWMxMzgyNWMzNWE5YjE2ZWQzZjA1ZTBlMjE4MzQzNDA1ZmI0ZTllMjFlNmRkYmFkNyZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmYWN0b3JfaWQ9MCZrZXlfaWQ9MCZyZXBvX2lkPTAifQ.16hlRLYkxCmeaueNjSK7nL-5UqpI5yr4H92efd2-QyY"> <img alt="gui2" width="1026" src="https://private-user-images.githubusercontent.com/7697454/292698581-c0d1db9f-f63d-4063-8c82-3cb172e0518f.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDM0NzAxODYsIm5iZiI6MTcwMzQ2OTg4NiwicGF0aCI6Ii83Njk3NDU0LzI5MjY5ODU4MS1jMGQxZGI5Zi1mNjNkLTQwNjMtOGM4Mi0zY2IxNzJlMDUxOGYucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQUlXTkpZQVg0Q1NWRUg1M0ElMkYyMDIzMTIyNSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyMzEyMjVUMDIwNDQ2WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YTFhYjFiMzI3ODU1YWZiYjQ4NGQzMWY3MGJmMTQ2OWY4NGRmZGYxZmI5NWViY2JjOWM5NTI0MzcwMTEwZjdkZSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmYWN0b3JfaWQ9MCZrZXlfaWQ9MCZyZXBvX2lkPTAifQ.L7zu_2-BR0tlzRgsQRs9o_kmZV1PpMq_KqKfyzMouPM">
> Works without issues here, I entered `2023-12-01` and it set the restore height to `3010228`. Please make a screenshot how it looks for you.

![image](https://github.com/monero-project/monero-gui/assets/106807841/e1ed8bd4-a89a-4748-abaa-71b399cf6e76)

![image](https://github.com/monero-project/monero-gui/assets/106807841/63019fc0-81f3-41ca-aae4-5db0fd5ccc31)


I use monero-gui-v0.18.3.1

# Action History
- Created by: developergames2d | 2023-12-24T23:00:24+00:00
- Closed at: 2023-12-25T00:30:45+00:00
