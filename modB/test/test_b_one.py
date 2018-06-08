# these imports should be necessary, but pytest seems to cache the imports
# from all the files it imported previously.
import modA.one
import modA.two
import modB.one
import modB.two


def test_a_one():
    assert modA.one.print_self() == "modA::one::print_self()"


def test_a_two():
    assert modA.two.print_self() == "modA::two::print_self()"


def test_b_one():
    assert modB.one.print_self() == "modB::one::print_self()"


def test_b_two():
    assert modB.two.print_self() == "modB::two::print_self()"
