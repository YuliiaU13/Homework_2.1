import pytest
from lesson_16.homework_lesson16 import TeamLead


@pytest.fixture
def team_lead():
    return TeamLead(
        name='Anna',
        salary=1500,
        department='IT-squad',
        programming_language='Python',
        team_size=6
    )

def test_employee_attributes(team_lead):
    assert team_lead.name == 'Anna'
    assert team_lead.salary == 1500


def test_manager_attributes(team_lead):
    assert team_lead.department == 'IT-squad'


def test_developer_attributes(team_lead):
    assert team_lead.programming_language == 'Python'


def test_team_size(team_lead):
    assert team_lead.team_size == 6
