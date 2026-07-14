"""Capability: deploy a release (GitHub tests -> Azure)."""


def deploy_release(release: dict, github, azure) -> dict:
    tests = github.run_tests(release["branch"])
    if tests["tests"] != "PASS":
        return {"status": "blocked", "reason": "tests failed"}
    deployed = azure.deploy(release["branch"])
    return {"status": "deployed", "tests": tests, "azure": deployed}
