import os
import subprocess


def rel_location():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    return __location__


def test_structureTool():

    tool_dir = os.path.realpath(os.path.join(rel_location(), ".."))
    test_input = os.path.join(tool_dir, "tests/testData/airports.xml")
    main_script = os.path.join(tool_dir, "main.py")
    test_output = os.path.join(tool_dir, "cpacsIO/cpacs_out.xml")

    old_cwd = os.getcwd()
    os.chdir(tool_dir)

    subprocess.run(["python", main_script, f"--cpacs_input={test_input}"], check=True)
    assert os.path.isfile(test_output)
    os.remove(test_output)

    os.chdir(old_cwd)
