import numpy as np

# PROJECT 1:

sensor_values = np.genfromtxt("sensor_data.csv", delimiter=",", skip_header=1, usecols=(1, 2, 3, 4))
print(sensor_values)

temp_readings = sensor_values[:, 0]
dist_readings = sensor_values[:, 1]
battery_levels = sensor_values[:, 2]
humidity_levels = sensor_values[:, 3]

print("Average Temperature:", np.mean(temp_readings))
print("Minimum Temperature:", np.min(temp_readings))
print("Maximum Temperature:", np.max(temp_readings))

print("\nAverage Distance:", np.mean(dist_readings))
print("Minimum Distance:", np.min(dist_readings))
print("Maximum Distance:", np.max(dist_readings))

print("\nAverage Battery:", np.mean(battery_levels))
print("Minimum Battery:", np.min(battery_levels))
print("Maximum Battery:", np.max(battery_levels))

print("\nAverage Humidity:", np.mean(humidity_levels))
print("Minimum Humidity:", np.min(humidity_levels))
print("Maximum Humidity:", np.max(humidity_levels))

time_column = np.genfromtxt("sensor_data.csv", delimiter=",", skip_header=1, usecols=(0), dtype=str)
print(time_column)
idx_max_temp = np.argmax(temp_readings)
print(idx_max_temp)
print("Time Of Max Temperature:", time_column[idx_max_temp])

battery_below_30_count = np.sum(battery_levels < 30)
print("Battery Less Than 30(count):", battery_below_30_count)

with open("sensor_data_output.csv", "w") as file:
    file.write(f"Average Temperature = {np.mean(temp_readings)}\n")
    file.write(f"Maximum Temperature = {np.max(temp_readings)}\n")
    file.write(f"Minimum Temperature = {np.min(temp_readings)}\n\n")

    file.write(f"Average Distance = {np.mean(dist_readings)}\n")
    file.write(f"Maximum Distance = {np.max(dist_readings)}\n")
    file.write(f"Minimum Distance = {np.min(dist_readings)}\n\n")

    file.write(f"Average Battery = {np.mean(battery_levels)}\n")
    file.write(f"Maximum Battery = {np.max(battery_levels)}\n")
    file.write(f"Minimum Battery = {np.min(battery_levels)}\n\n")

    file.write(f"Average Humidity = {np.mean(humidity_levels)}\n")
    file.write(f"Maximum Humidity = {np.max(humidity_levels)}\n")
    file.write(f"Minimum Humidity = {np.min(humidity_levels)}\n\n")

    file.write(f"Time Of Max Temperature = {time_column[idx_max_temp]}\n\n")

    file.write(f"Battery Less Than 30(count) = {battery_below_30_count}\n")


# PROJECT 2:

robot_coordinates = np.genfromtxt("robot_path.csv", delimiter=",", skip_header=1)
print(robot_coordinates)

coordinate_differences = np.diff(robot_coordinates, axis=0)
step_distances = np.sqrt(np.sum(coordinate_differences ** 2, axis=1))
path_length = np.sum(step_distances)

print("Total Distance:", path_length)

distance_from_start = np.sqrt(np.sum(robot_coordinates ** 2, axis=1))
farthest_index = np.argmax(distance_from_start)
print("Farthest Point From Origin:", robot_coordinates[farthest_index])

has_revisited = "YES" if len(np.unique(robot_coordinates, axis=0)) < len(robot_coordinates) else "NO"
print("Revisited:", has_revisited)

with open("robot_path_output.csv", "w") as file:
    file.write(f"Total Distance : {path_length}\n")
    file.write(f"Farthest Point From Origin : {robot_coordinates[farthest_index]}\n")
    file.write(f"Revisited = {has_revisited}\n")
