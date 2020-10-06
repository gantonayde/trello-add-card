#!/usr/bin/python3

import requests
import argparse


example_board = 'yXWd2EX0'
labels = ('green', 'yellow', 'orange', 'red', 'purple', 'blue')
key = 'a6848b7ec5352326086c073b86c1d8a4'
token = 'd493b285a7f745f38f31b8f28a95125f42455294d8ad0a1c43584b1d7b98889b'

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
parser.add_argument("-c", "--card", help="card text", required=True, metavar='')
parser.add_argument("-l", "--list", help="create/add to a list name", required=True, metavar='')
group.add_argument("-b", "--board", help=f"existing board ID (default is {example_board})",
                                                     default=f"{example_board}", metavar='')
group.add_argument("-nb", "--newboard", help="name a new board", metavar='')
parser.add_argument("-ct", "--comment", help="add a comment to the card", metavar='')
parser.add_argument("-lb", "--label", help=f"add colour labels to the card {labels}", nargs="+", choices=labels, metavar='')
args = parser.parse_args()


def create_board(board_name):
    url = "https://api.trello.com/1/boards/"
    querystring = {"name": board_name, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
    board_id = response.json()["shortUrl"].split("/")[-1].strip()
    return board_id


def create_list(board_id, list_name):
    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    querystring = {"name": list_name, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
    list_id = response.json()["id"]
    return list_id


def create_card(list_id, card_name):
    url = "https://api.trello.com/1/cards"
    querystring = {"name": card_name, "idList": list_id, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
    card_id = response.json()["id"]
    return card_id


def create_comment(card_id, comment):
    url = f"https://api.trello.com/1/cards/{card_id}/actions/comments"
    querystring = {'text': f'{comment}', "key": key, "token": token}
    requests.request("POST", url, params=querystring)
    return


def add_label(card_id, label_id):
    url = f"https://api.trello.com/1/cards/{card_id}/idLabels"
    querystring = {'value': label_id, "key": key, "token": token}
    requests.request("POST", url, params=querystring)
    return


def get_labels(board_id):
    url = f"https://api.trello.com/1/boards/{board_id}/labels"
    querystring = {"key": key, "token": token}
    response = requests.request("GET", url, params=querystring)
    labels_dict = {}
    for i in response.json():
        labels_dict[i['color']] = i['id']
    return labels_dict


def find_lists(board_id, list_name):
    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    querystring = {"key": key, "token": token}
    response = requests.request("GET", url, params=querystring)
    list_id = None
    for board_list in response.json():
        if board_list['name'] == list_name:
            list_id = board_list['id']
            break
    return list_id

def main(args):
    if args.newboard:
        board_id = create_board(args.newboard)
    else:
        board_id = args.board

    list_id = find_lists(board_id, args.list)
    if list_id is None:
        list_id = create_list(board_id, args.list)
    card_id = create_card(list_id, args.card)

    if args.comment:
        create_comment(card_id, args.comment)
    if args.label:
        labels_dict = get_labels(board_id)
        for label in args.label:
            add_label(card_id, labels_dict[label])

if __name__ == "__main__":
    main(args)
