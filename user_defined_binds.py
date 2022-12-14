from bind_skel import macro_class, run_as_user


def test():
    print("Hello!")


@macro_class
class Macros:
    """Macros that will be used & executed for a specific keyboard. In order to get the keyboard name,
    execute program with "dump device data" flag to dump the exact device name & data, or
    use this command on Unix (look for sysrq in the handler field):
    cat /proc/bus/input/devices
    Please keep in mind that in order to create multiple modes for the same keyboard, a different class (with the same
    KEYBOARD_NAME value) must be provided.
    To create a custom controller, please take a look into the DefaultController class provided in main.py.
    If you want to extend the function of the controller to more axis, you should override get_input_event_type.
    (https://www.kernel.org/doc/html/v4.17/input/event-codes.html)"""

    """Name of the keyboard we're going to catch the input from."""
    KEYBOARD_NAME = "USB Keyboard"

    """Macros to execute when KEY_DOWN is triggered."""
    MACROS_DOWN = {
        ("KEY_GRAVE",): test,
        ("KEY_GRAVE", "KEY_TAB"): lambda: print("World~")
    }

    """Macros to execute when KEY_UP is triggered."""
    MACROS_UP = {
        # open processes THIS WAY! otherwise they will run as root!!!
        ("KEY_GRAVE",): lambda: run_as_user("gnome-terminal")
    }

    """Macros to execute when KEY_HOLD is triggered."""
    MACROS_HOLD = {
        ("KEY_GRAVE", "KEY_1"): lambda: print("Holding!!"),
        ("KEY_GRAVE", ): lambda: print("amogus")
    }

    """If CONTROLLER is not defined, the default controller will be used for this keyboard."""
    CONTROLLER = None
