# -*- coding: utf-8 -*-
from app import app, db

@app.route('/api/v1/proveit', methods=['GET'])
@app.route('/api/v1/proveit/<int:proveit_id>', methods=['GET', 'POST', 'UPDATE', 'DELETE'])
def proveit(proveit_id=-1):
    if proveit_id is not -1:
        return 'this is the proveit id you sent ' + str(proveit_id)
    else:
        return 'we shoud return all'
