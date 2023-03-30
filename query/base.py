import csv, io


class QueryBase:
    # summary

    def get_run_matches_paginated(self, run, familyId=None, familyName=None, page=1, perPage=20, **url_params):
        if (familyId and familyName):
            raise ValueError('Cannot specify both familyId and familyName.')
        run_id = run
        if familyId:
            table = self.table_map['sequence']
            query = (table.query
                .filter(table.run_id == run_id)
                .filter(table.family_id == familyId)
                .order_by(table.score.desc())
                .order_by(table.n_reads.desc()))
        elif familyName:
            table = self.table_map['sequence']
            query = (table.query
                .filter(table.run_id == run_id)
                .filter(table.family_name == familyName)
                .order_by(table.score.desc())
                .order_by(table.n_reads.desc()))
        else:
            table = self.table_map['family']
            query = (table.query
                .filter(table.run_id == run_id)
                .order_by(table.score.desc())
                .order_by(table.n_reads.desc()))
        query = apply_filters(query, table, **url_params)
        return query.paginate(page=int(page), per_page=int(perPage))

    # matches

    def get_table_key(self, **url_params):
        for key in self.table_map:
            if key in url_params:
                return key

    def get_matches_file(self, **url_params):
        key = self.get_table_key(**url_params)
        value = url_params.pop(key)
        table = self.table_map[key]
        filter_col = getattr(table, table.filter_col_name)
        select_column_names = ['run_id', table.filter_col_name, 'score', 'percent_identity', 'n_reads']
        select_columns = [getattr(table, name) for name in select_column_names]
        query = (table.query
            .filter(filter_col == value)
            .with_entities(*select_columns))
        query = apply_filters(query, table, **url_params)
        matches = query.all()
        f = io.StringIO()
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(select_column_names)
        for match in matches:
            writer.writerow(match)
        f.seek(0)
        return f.read()

    def get_matches_paginated(self, page=1, perPage=20, **url_params):
        key = self.get_table_key(**url_params)
        value = url_params.pop(key)
        table = self.table_map[key]
        filter_col = getattr(table, table.filter_col_name)
        query = (table.query
            .filter(filter_col == value)
            .order_by(table.score.desc())
            .order_by(table.n_reads.desc())
            .order_by(table.run_id.desc()))
        query = apply_filters(query, table, **url_params)
        return query.paginate(page=int(page), per_page=int(perPage))

    # counts

    def get_count_table_key(self, **url_params):
        for key in self.count_table_map:
            if key in url_params:
                return key

    def get_counts(self, **url_params):
        key = self.get_count_table_key(**url_params)
        value = url_params.pop(key)
        table = self.count_table_map[key]
        filter_col = getattr(table, table.filter_col_name)
        select_column_names = ['score', 'percent_identity', 'count']
        select_columns = [getattr(table, name) for name in select_column_names]
        query = (table.query
            .filter(filter_col == value)
            .with_entities(*select_columns))
        counts = query.all()
        result_json = [entry._asdict() for entry in counts]
        return result_json

    # list

    def get_list(self, query_type, **url_params):
        table = self.list_table_map[query_type]
        filter_col = getattr(table, table.filter_col_name)
        select_column_names = [table.filter_col_name]
        if query_type == 'sequence':
            select_column_names.append('virus_name')
        select_columns = [getattr(table, name) for name in select_column_names]
        query = (table.query
            .with_entities(*select_columns))
        values_list = query.all()
        if query_type == 'sequence':  # {accession: name}
            return {entry[0]: entry[1] for entry in values_list}
        return {entry[0]: None for entry in values_list}


def apply_filters(query, model, scoreMin=None, scoreMax=None, identityMin=None, identityMax=None):
    if scoreMin:
        query = query.filter(model.score >= int(scoreMin))
    if scoreMax:
        query = query.filter(model.score <= int(scoreMax))
    if identityMin:
        query = query.filter(model.percent_identity >= int(identityMin))
    if identityMax:
        query = query.filter(model.percent_identity <= int(identityMax))
    return query
