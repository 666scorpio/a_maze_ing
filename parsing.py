def value_supposed(key, value, line, line_number):
    if key == "WIDTH":
        try:
            n = int(value)
        except ValueError:
            raise ValueError(f"Line {line_number}: WIDTH must be an integer\n"
                             f"→ {line}")
        if n <= 0:
            raise ValueError(
                f"Line {line_number}: WIDTH must be greater than 0\n"
                f"→ {line}")
    elif key == "HEIGHT":
        try:
            n = int(value)
        except ValueError:
            raise ValueError(
                f"Line {line_number}: HEIGHT must be an integer\n"
                f"→ {line}")
        if n <= 0:
            raise ValueError(
                f"Line {line_number}: HEIGHT must be greater than 0\n"
                f"→ {line}"
            )
    elif key == "ENTRY" or key == "EXIT":
        try:
            x, y = tuple(map(int, value.split(",")))
        except ValueError:
            raise ValueError(
                f"Line {line_number}: {key} must be in format"
                " x,y with integers\n"
                f"→ {line}"
            )
    elif key == "PERFECT" and (not value == "True" and not value == "False"):
        raise ValueError(
            f"Line {line_number}: PERFECT must be 'True' or 'False'\n"
            f"→ {line}"
        )
    elif key == "SEED":
        try:
            int(value)
        except ValueError:
            raise ValueError(
                f"Line {line_number}: SEED must be an integer\n"
                f"→ {line}"
            )


def parse_config(path):
    try:
        with open(path) as file:
            lines = file.readlines()
            keys_required = [
                "WIDTH", "HEIGHT", "ENTRY", "EXIT",
                "OUTPUT_FILE", "PERFECT"]
            acceptable_keys = [
                "WIDTH", "HEIGHT", "ENTRY", "EXIT",
                "OUTPUT_FILE", "PERFECT", "SEED"]
            config = {}
            for line_number, line in enumerate(lines, 1):
                line = line.split("#", 1)[0].strip()
                if not line:
                    continue
                if line.startswith("#"):
                    continue
                if "=" not in line:
                    raise ValueError(
                        f"Line {line_number}: Invalid syntax"
                        " (expected KEY=VALUE)\n"
                        f"→ {line}"
                                    )
                key, value = line.split("=", 1)
                key = key.strip()
                if key not in acceptable_keys:
                    raise ValueError(
                        f"Line {line_number}: Unknown configuration "
                        f"key '{key}'\n"
                        f"→ {line}"
                                    )
                value = value.strip()
                value_supposed(key, value, line, line_number)
                if key in ("WIDTH", "HEIGHT", "SEED"):
                    config[key] = int(value)
                elif key in ("ENTRY", "EXIT"):
                    coordinates = tuple(map(int, value.split(",")))
                    config[key] = coordinates
                else:
                    config[key] = value
            missing_keys = []
            missing_keys = [
                key for key in keys_required
                if key not in config
                            ]
            if missing_keys:
                raise ValueError(
                        "Missing required key(s): " +
                        ", ".join(missing_keys)
                                )
            for point_key in ("ENTRY", "EXIT"):
                x, y = config[point_key]
                if x < 0 or x >= config["WIDTH"]\
                    or y < 0 or y >= config["HEIGHT"]:
                    raise ValueError(
                        f"{point_key} coordinates out of bounds "
                        f"(0 ≤ x < WIDTH, 0 ≤ y < HEIGHT)"
                                    )
            return config

    except Exception as error:
        print(f"ERROR: {error}")
        return {}


config = parse_config("file")
for key, value in config.items():
    print(key + "=" + str(value))
