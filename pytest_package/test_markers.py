'''
Markers :   To group the testcases, we go for markers
There are 2 types of markers
    *   custom marker
    *   inbuilt marker

'''

import pytest

# def test_login():
#     print("login executing")
#
# @pytest.mark.sanity
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.sanity
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## In terminal
# ## pytest test_markers.py -vs -m="sanity"
# ## collected 4 items / 2 deselected / 2 selected
# ## test_markers.py::test_reg       reg executing           PASSED
# ## test_markers.py::test_signup    signup executing        PASSED

##############################################################################################################

# @pytest.mark.smoke
# def test_login():
#     print("login executing")
#
# @pytest.mark.sanity
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.regression
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.smoke
# def test_logout():
#     print("logout executing")
#
# ## In terminal
# ## pytest test_markers.py -vs -m="sanity"               --> test_reg will execute
# ## pytest test_markers.py -vs -m="smoke"                --> test_login and test_logout will execute
# ## pytest test_markers.py -vs -m="regression"           --> test_signup will execute
# ## pytest test_markers.py -vs -m="sanity and smoke"     --> collected 4 items / 4 deselected / 0 selected
# ## pytest test_markers.py -vs -m="sanity or smoke"      --> test_login, test_reg, test_logout will execute

##############################################################################################################

# @pytest.mark.sanity
# @pytest.mark.smoke
# def test_login():
#     print("login executing")
#
# @pytest.mark.regression
# @pytest.mark.sanity
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.regression
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.sanity
# @pytest.mark.smoke
# def test_logout():
#     print("logout executing")
#
# ## In terminal
# ## pytest test_markers.py -vs -m="sanity"                   --> test_login, test_reg, test_logout will execute
# ## pytest test_markers.py -vs -m="smoke"                    --> test_login and test_logout will execute
# ## pytest test_markers.py -vs -m="regression"               --> test_reg and test_signup will execute
# ## pytest test_markers.py -vs -m="sanity and smoke"         --> test_login and test_logout will execute
# ## pytest test_markers.py -vs -m="sanity and regression"    --> test_reg will execute
# ## pytest test_markers.py -vs -m="smoke and regression"     --> 0
# ## pytest test_markers.py -vs -m="sanity or smoke"          --> test_login, test_reg, test_logout will execute
# ## pytest test_markers.py -vs -m="sanity or regression"     --> All 4 will execute
# ## pytest test_markers.py -vs -m="regression or smoke"      --> All 4 will execute
# ## pytest test_markers.py -vs -m="not smoke"                --> test_reg and test_signup will execute
# ## pytest test_markers.py -vs -m="not sanity"               --> test_signup will execute
# ## pytest test_markers.py -vs -m="not regression"           --> test_login and test_logout will execute

##############################################################################################################

# @pytest.mark.sanity
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## pytest test_markers.py -vs -m="sanity"   --> All 4 will execute

##############################################################################################################

@pytest.mark.regression
class TestSample:

    @pytest.mark.sanity
    def test_login(self):
        print("login executing")

    def test_reg(self):
        print("reg executing")

    @pytest.mark.smoke
    def test_signup(self):
        print("signup executing")

    def test_logout(self):
        print("logout executing")





















































