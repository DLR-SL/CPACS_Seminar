import os
import subprocess
import shutil

# Remove files after tests?:
clean = True

def rel_location():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    return __location__

def test_toolRun():

    # Copy input file to cpacsIO directory:
    src = os.path.join(rel_location(),"testData/CPACS_in.xml")
    dst = os.path.join(rel_location(),"../cpacsIO/CPACS_in.xml")
    shutil.copyfile(src,dst)

    # Run the tool:
    subprocess.run(["python", "run.py"])

    # Check the result:
    out = os.path.join(rel_location(),"../cpacsIO/CPACS_out.xml")
    assert os.path.isfile(out)

    # Clean:
    if clean:
        for file in [dst,out]:
            os.remove(file)
