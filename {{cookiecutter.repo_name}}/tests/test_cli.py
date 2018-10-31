from subprocess import check_output


def test_cli():
    """Test cli"""
    result = run_cmd("helloworld test")
    assert result == " INFO - Running test function"

def run_cmd(cmd):
    """Run a shell command and return output"""
    return check_output(cmd, shell=True).decode('utf-8').rstrip('\n')
