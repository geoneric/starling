import os
from test.test_case import TestCase
from starling.geoserver.catalog import *


class CatalogTest(TestCase):

    geoserver_uri = os.environ.get("GEOSERVER_URI")
    geoserver_username = "admin"
    geoserver_password = "geoserver"


    def setUp(self):
        self.catalog = Catalog(
            self.geoserver_uri,
            username=self.geoserver_username,
            password=self.geoserver_password)


    def tearDown(self):
        del self.catalog


    def recreate_workspace(self,
            workspace_name):

        if self.catalog.workspace_exists(workspace_name):
            self.catalog.delete_workspace(workspace_name, True)

        self.assertFalse(self.catalog.workspace_exists(workspace_name))

        self.catalog.create_workspace(workspace_name)


    def test_workspace(self):

        workspace_name = "my_workspace"
        self.recreate_workspace(workspace_name)

        workspaces = self.catalog.workspaces()

        self.assertTrue(isinstance(workspaces, list))

        self.assertTrue(self.catalog.workspace_exists(workspace_name))

        workspace = self.catalog.workspace(workspace_name)

        self.assertTrue("dataStores" in workspace)
        self.assertTrue("wmsStores" in workspace)
        self.assertTrue("coverageStores" in workspace)

        self.assertTrue("name" in workspace)
        self.assertEqual(workspace["name"], workspace_name)


    def test_coverage_store(self):

        workspace_name = "my_workspace"
        self.recreate_workspace(workspace_name)

        coverage_store_name = "my_coverage_store"

        self.assertFalse(self.catalog.coverage_store_exists(workspace_name,
            coverage_store_name))

        coverage_store_type = "GeoTIFF"
        coverage_pathname = "my_data/blah.tif"

        self.catalog.create_coverage_store(workspace_name,
            coverage_store_name, type=coverage_store_type,
            pathname=coverage_pathname)

        coverage_stores = self.catalog.coverage_stores(workspace_name)

        self.assertTrue(isinstance(coverage_stores, list))

        self.assertTrue(self.catalog.coverage_store_exists(
            workspace_name, coverage_store_name))

        coverage_store = self.catalog.coverage_store(workspace_name,
            coverage_store_name)

        self.assertTrue("name" in coverage_store)
        self.assertEqual(coverage_store["name"], coverage_store_name)

        self.assertTrue("type" in coverage_store)
        self.assertEqual(coverage_store["type"], coverage_store_type)

        self.assertTrue("url" in coverage_store)
        self.assertEqual(coverage_store["url"], "file:{}".format(
            coverage_pathname))

        self.assertTrue("enabled" in coverage_store)
        self.assertTrue(coverage_store["enabled"])

        self.assertTrue("workspace" in coverage_store)
        self.assertEqual(coverage_store["workspace"]["name"], workspace_name)

        self.assertTrue("coverages" in coverage_store)

        self.catalog.delete_coverage_store(workspace_name,
            coverage_store_name, True)

        self.assertFalse(self.catalog.coverage_store_exists(workspace_name,
            coverage_store_name))


    def test_layer(self):
        workspace_name = "my_workspace"
        self.recreate_workspace(workspace_name)

        coverage_store_name = "my_coverage_store"
        coverage_store_type = "GeoTIFF"
        coverage_pathname = "my_data/blah.tif"

        self.catalog.create_coverage_store(workspace_name,
            coverage_store_name, type=coverage_store_type,
            pathname=coverage_pathname)




    def test_style(self):
        pass


if __name__ == "__main__":
    unittest.main()
