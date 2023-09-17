# API

/predict POST
    outside_temp
    elevator_temp
    elevator_speed
    door_speed
    usage_time
returns
	probability of elevator failure

/ GET
returns
	"Hello World"

/notify_technicians POST
    elevator_id
returns
    "OK"

# Interpreting the API

Needs routine maintenance if probability of failure is > 20%

Needs emergency maintenance if probability of failure is > 40%

No maintenance needed if probability of failure is < 20%

Order of priority can be set directly by the % failure.

# Example Outputs

- 305.8,309.4,1342,362.4,0 - 10%
- 305.8,309.4,1342,162.4,0 - 25%
- 355.8,309.4,1342,162.4,0 - 28%
- 285.8,309.4,1342,162.4,0 - 11%
- 305.8,309.4,2342,162.4,0 - 20%
- 305.8,302.4,1342,162.4,0 - 12%
- 205.8,302.4,1342,162.4,0 - 11%
- 301.8,302.4,1942,162.4,10 - 11%
- 305.8,309.4,1342,362.4,0 - 10%
- 305.8,309.4,1342,162.4,0 - 25%
- 355.8,309.4,1342,162.4,0 - 28%
- 285.8,309.4,1342,162.4,0 - 11%
- 303.8,310.4,1542,162.4,10 - 11%