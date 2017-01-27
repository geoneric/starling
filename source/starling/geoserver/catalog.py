import json
import requests


class Catalog(object):

    def __init__(self,
            uri,
            username,
            password):
        self.uri = uri
        self.auth = (username, password)


    def workspaces(self):

        headers = {
            "Accept": "application/json"
        }
        response = requests.get(
            "{}/workspaces".format(self.uri),
            headers=headers,
            auth=self.auth)

        if response.status_code != 200:
            raise RuntimeError(response.text)

        data = response.json()
        workspaces = data["workspaces"]["workspace"]

        return workspaces


    def workspace(self,
            name):

        headers = {
            "Accept": "application/json"
        }
        response = requests.get(
            "{}/workspaces/{}".format(self.uri, name),
            headers=headers,
            auth=self.auth)

        if response.status_code != 200:
            raise RuntimeError(response.text)

        data = response.json()
        workspace = data["workspace"]

        return workspace


    def workspace_exists(self,
            name):

        parameters = {
            "quietOnNotFound": "true"
        }
        response = requests.get(
            "{}/workspaces/{}".format(self.uri, name),
            params=parameters,
            auth=self.auth)

        return response.status_code == 200


    def create_workspace(self,
            name):

        headers = {
            "Content-type": "application/json"
        }
        payload = {
            "workspace": {
                "name": name
            }
        }
        response = requests.post(
            "{}/workspaces".format(self.uri),
            headers=headers,
            data=json.dumps(payload),
            auth=self.auth)

        if response.status_code != 201:
            raise RuntimeError(response.text)


    def delete_workspace(self,
            name,
            recurse=False):

        headers = {
            "Content-type": "application/json"
        }
        parameters = {
            "recurse": "true" if recurse else "false"
        }
        response = requests.delete(
            "{}/workspaces/{}".format(self.uri, name),
            headers=headers,
            params=parameters,
            auth=self.auth)

        if response.status_code != 200:
            raise RuntimeError(response.text)


    def coverage_stores(self,
            workspace_name):

        headers = {
            "Accept": "application/json"
        }
        response = requests.get(
            "{}/workspaces/{}/coveragestores".format(self.uri, workspace_name),
            headers=headers,
            auth=self.auth)

        if response.status_code != 200:
            raise RuntimeError(response.text)


        data = response.json()
        coverage_stores = data["coverageStores"]["coverageStore"]

        return coverage_stores


    def coverage_store(self,
            workspace_name,
            name):

        headers = {
            "Accept": "application/json"
        }
        response = requests.get(
            "{}/workspaces/{}/coveragestores/{}".format(self.uri,
                workspace_name, name),
            headers=headers,
            auth=self.auth)

        if response.status_code != 200:
            raise RuntimeError(response.text)

        data = response.json()
        coverage_store = data["coverageStore"]

        return coverage_store


    def coverage_store_exists(self,
            workspace_name,
            name):

        parameters = {
            "quietOnNotFound": "true"
        }
        response = requests.get(
            "{}/workspaces/{}/coveragestores/{}".format(self.uri,
                workspace_name, name),
            params=parameters,
            auth=self.auth)

        return response.status_code == 200


    def create_coverage_store(self,
            workspace_name,
            name,
            type,
            pathname):

        headers = {
            "Content-type": "application/json"
        }
        payload = {
            "coverageStore": {
                "name": name,
                "type": type,
                "enabled": "true",
                "workspace": workspace_name,
                "url": "file:{}".format(pathname),
            }
        }

        response = requests.post(
            "{}/workspaces/{}/coveragestores".format(self.uri,
                workspace_name),
            headers=headers,
            data=json.dumps(payload),
            auth=self.auth)

        if response.status_code != 201:
            raise RuntimeError(response.text)


    def delete_coverage_store(self,
            workspace_name,
            name,
            recurse=False):

        headers = {
            "Content-type": "application/json"
        }
        parameters = {
            "recurse": "true" if recurse else "false"
        }
        response = requests.delete(
            "{}/workspaces/{}/coveragestores/{}".format(self.uri,
                workspace_name, name),
            headers=headers,
            params=parameters,
            auth=self.auth)

        if response.status_code != 200:
            raise RuntimeError(response.text)
