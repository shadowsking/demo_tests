import logging

logger = logging.getLogger(__name__)


def print_hello():
    print("Hello Capsys")


def log_hello():
    logger.error("Hello Caplog")


def test_output(capsys):
    print_hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello Capsys\n"


def test_log(caplog):
    with caplog.at_level(logging.ERROR):
        log_hello()

    assert "Hello Caplog" in caplog.text
