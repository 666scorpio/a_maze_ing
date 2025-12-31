def value_supposed(key, value, line):
    if key == "WIDTH":
        try:
            n = int(value)
        except ValueError:
            raise ValueError("the WIDTH must be number" + line)
        if n <= 0:
                raise ValueError("the WIDTH must be more than 0"
                                 " and not negative")        
    if key == "HEIGHT":
        try:
            n = int(value)
        except ValueError:
            raise ValueError("the HEIGHT must be number" + line)
        if n <= 0:
            raise ValueError("the HEIGHT must be more than 0"
                             " and not negative")
    if key == "ENTRY" or key == "EXIT":
        try:
            x, y = tuple(map(int, value.split(",")))
        except ValueError:
            raise ValueError(f"Invalid coordinates: {value}"
                              " must be numbers")
    if key == "PERFECT" and (not value == "True" and not value == "False"):
        raise ValueError("the PERFECT must be True or False")
    if key == "SEED":
        try:
            int(value)
        except ValueError:
            raise ValueError("the SEED must be number" + line)

def parse_config(path):
    try:
        with open(path) as file:
            lines = file.readlines()
            keys_required = [
                "WIDTH", "HEIGHT", "ENTRY", "EXIT",
                "OUTPUT_FILE", "PERFECT"]
            config = {}
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                if line.startswith("#"):
                    continue
                if "=" not in line:
                    raise ValueError("bad syntax :" + line)
                key, value = line.split("=", 1)
                key = key.strip()
                if key not in keys_required:
                    raise ValueError("bad syntax :" + line)
                value = value.strip()
                value_supposed(key, value, line)
                if key in ("WIDTH", "HEIGHT", "SEED"):
                    config[key] = int(value)
                elif key in ("ENTRY", "EXIT"):
                    coordinates = tuple(map(int, value.split(",")))
                    config[key] = coordinates
                else:
                    config[key] = value
            for key in keys_required:
                if key not in config:
                    raise ValueError(f"Missing required key in config file: {key}")
            for point_key in ("ENTRY", "EXIT"):
                x, y = config[point_key]
                if x < 0 or x >= config["WIDTH"]\
                      or y < 0 or y >= config["HEIGHT"]:
                    raise ValueError(f"{point_key} coordinates out of bounds")
            return config

    except Exception as error:
        print(f"ERROR: {error}")
        return {}

config = parse_config("file")
for key, value in config.items():
    print(key + "=" + str(value))