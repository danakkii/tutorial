"""
Qt Linguist and its related tools can be used to provide translations for applications.
"""

count = len(self._list_widget.selectionModel().selectedRows())
message = self.tr("%n language(s) selected", "", count)