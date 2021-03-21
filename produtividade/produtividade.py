# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import Optional, List

from github import Github
from github.StatsContributor import StatsContributor
from github.Repository import Repository
# import fire
import sys
import getopt
import pandas as pd
import numpy as np
import csv
from pandas import DataFrame

DELIMITER = ','
# GITHUB_ACCESS_TOKEN = '76720cbff3230a29466528a0fcc699153eb93471'
GITHUB_ACCESS_TOKEN = 'a7328bea17b20dba43bb48b2c0fdb4b75962f8a1'


def get_stats_contributor_by_contributor_name(name_contributor: str, stats_contributors: list):
    for stats_contributor in stats_contributors:
        if stats_contributor.author.name == name_contributor:
            return stats_contributor

    return


def get_repo_total_commits(repo: Repository):
    total_commits = 0

    contributors = repo.get_contributors()

    for contributor in contributors:
        total_commits += contributor.contributions

    return total_commits


def get_contributor_productivity(contributor_contributions: dict, repo_total_lines: int, contributor_commits: int,
                                 repo_total_commits: int):
    if contributor_contributions is None:
        return 0

    contributor_contribution = contributor_contributions.get("added_lines") - contributor_contributions.get(
        "removed_lines")

    return ((contributor_contribution + contributor_commits) / (repo_total_lines + repo_total_commits))


def get_repo_total_lines(stats_contributors):
    total_lines = 0

    for stats_contributor in stats_contributors:
        contribution = get_contributor_total_contributions(stats_contributor)
        total_lines += contribution.get("added_lines") - contribution.get("removed_lines")

    return total_lines


def get_contributor_total_contributions(stats_contributor: StatsContributor):
    if stats_contributor is None:
        return

    added_lines = 0
    removed_lines = 0

    for week in stats_contributor.weeks:
        added_lines += week.a
        removed_lines += week.d

    return {
        'added_lines': added_lines,
        'removed_lines': removed_lines
    }


def github_fetch_repo_details(name):
    # Use a breakpoint in the code line below to debug your script.
    # First create a Github instance:

    # using an access token
    g = Github(GITHUB_ACCESS_TOKEN)

    repo_contributions = []

    try:
        repo = g.get_repo(name)
        statsContributors: Optional[List[StatsContributor]] = repo.get_stats_contributors()
        total_commits = get_repo_total_commits(repo)
        total_lines = get_repo_total_lines(statsContributors)

        print('REPO name: ', repo.name)
        print('REPO total number of commits: ', total_commits)
        print('REPO total lines: ', total_lines)
        print('REPO contributors: ')

        for contributor in repo.get_contributors():
            contributor_repo_contributions = get_contributor_total_contributions(
                get_stats_contributor_by_contributor_name(contributor.name, statsContributors)
            )

            productivity = get_contributor_productivity(contributor_repo_contributions, total_lines,
                                                        contributor.contributions.real,
                                                        total_commits)
            print('  ->', contributor.name, '(', contributor.login, '),',
                  'number commits: ', contributor.contributions.real,
                  ', repo contributions:', contributor_repo_contributions,
                  ', contributor productivity: ', productivity,
                  )

            repo_contributions = [name, contributor.login, productivity]

    except:
        print("REPO not found")

    return repo_contributions


def calcProductivity(data):
    productivity = []

    for index, row in enumerate(data):
        #githubreponame = data[index][len(data[0])-1]
        githubreponame = "josecbraz/LI"
        print(index, row)

        print('\nGithub repo name:', githubreponame)

        repo_contributions = github_fetch_repo_details(githubreponame)
        print(repo_contributions)

        print("Productivity of contributors of repo ", githubreponame, "\n  ->", repo_contributions)
        productivity.append(repo_contributions)

    return productivity


def readInputFileCSV(inputFile):
    data = []

    with open(inputFile) as F:
        for linha in F:
            lineArray = linha.split(DELIMITER)
            data.append(lineArray)

    data.pop(0)

    return data


def addStudentID(productivity, data):
    print('data size', len(data))
    print('prod size', len(productivity))
    print(productivity)
    print(data)
    if len(productivity) == 0 | len(data) == 0:
        return productivity

    for row in productivity:
        indexes = []

        if len(row) > 0:
            indexes = [(index, line.index(row[1])) for index, line in enumerate(data) if row[1] in line]

        if len(indexes) > 0:
            line = indexes[0][0]
            column = indexes[0][1]

            row.insert(0, data[line][column-2])

    print(productivity)
    return productivity


def createCSVFile(productivity):
    header = [["StudentID", "GitHubGrupo", "User", "Produtividade"]]
    if len(header[0]) != len(productivity[0]):
        sys.exit(2)

    row_list = np.concatenate((header, productivity))

    with open('produtividade.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)


def main(argv):
    print('reading file')
    inputfile = ''

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile="])
    except getopt.GetoptError:
        print('produtividade.py -i <inputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('produtividade.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
    print('Input file is "', inputfile)

    data = readInputFileCSV(inputfile)
    productivity = calcProductivity(data)
    productivity = addStudentID(productivity, data)
    createCSVFile(productivity)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(sys.argv[1:])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
