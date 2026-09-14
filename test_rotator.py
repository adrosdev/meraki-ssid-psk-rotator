from rotator import selected_networks
from rotator import Network


def test_reads_clean_names(tmp_path):
    file = tmp_path / "selected.txt"
    file.write_text("branch1\nbranch2\n")

    result = selected_networks(file)

    assert result == ["branch1", "branch2"]


def test_skips_blanks_and_strips_spaces(tmp_path):
    file = tmp_path / "selected.txt"
    file.write_text("branch1  \n\n  branch2\n")

    result = selected_networks(file)

    assert result == ["branch1", "branch2"]


def test_missing_file_returns_empty_list(tmp_path):
    result = selected_networks(tmp_path / "does_not_exist.txt")

    assert result == []


def test_new_network_starts_pending():
    net = Network("branch1", "N_123")

    assert net.status == "pending"
    assert net.name == "branch1"


def test_statuses_reconcile():
    fleet = [Network("a", "N_1"), Network("b", "N_2"), Network("c", "N_3")]
    fleet[0].status = "rotated"
    fleet[1].status = "failed"
    fleet[2].status = "skipped"

    rotated = [n for n in fleet if n.status == "rotated"]
    failed = [n for n in fleet if n.status == "failed"]
    skipped = [n for n in fleet if n.status == "skipped"]

    assert len(rotated) + len(failed) + len(skipped) == len(fleet)
