from app.database import engine
from app.response import response


def getUser(i_id):
    with engine.connect() as conn:
        query = conn.execute(
            "SELECT id_user"
            " FROM user"
            " WHERE id_user = '" + i_id + "'"
        ).fetchall()
        if len(query) < 1:
            return response(404, "Nomor tidak ditemukan", None)
        elif len(query) > 1:
            return response(409, "Nomor duplikat", None)
        query = conn.execute(
            "SELECT"
            "id_user ID_User,"
            "username UserName,"
            "nama_depan NamaDepan,"
            "nama_belakang NamaBelakang,"
            "role Role"
            "from user"
            "where id_user =  '" + query[0].id_user + "'"
        ).fetchall()
        return response(0, "Success", query)
