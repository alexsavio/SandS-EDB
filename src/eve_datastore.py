from flask_security.datastore import Datastore, UserDatastore
from flask_security.datastore.utils import get_identity_attributes

class EveDatastore(Datastore):

    def put(self, model):
        model.save()
        return model

    def delete(self, model):
        model.delete()


class EveUserDataStore(UserDatastore):
    """An Eve datastore implementation for Flask-Security that assumes
    the use of the Flask-MongoEngine extension.
    """
    def __init__(self, db, user_model, role_model):
        EveDatastore.__init__(self, db)
        UserDatastore.__init__(self, user_model, role_model)

    def get_user(self, identifier):
        from eve.validation import ValidationError
        try:
            return self.user_model.objects(id=identifier).first()
        except ValidationError:
            pass
        for attr in get_identity_attributes():
            query_key = '%s__iexact' % attr
            query = {query_key: identifier}
            rv = self.user_model.objects(**query).first()
            if rv is not None:
                return rv

    def find_user(self, **kwargs):
        try:
            from mongoengine.queryset import Q, QCombination
        except ImportError:
            from mongoengine.queryset.visitor import Q, QCombination
        from mongoengine.errors import ValidationError

        queries = map(lambda i: Q(**{i[0]: i[1]}), kwargs.items())
        query = QCombination(QCombination.AND, queries)
        try:
            return self.user_model.objects(query).first()
        except ValidationError:
            return None

    def find_role(self, role):
        return self.role_model.objects(name=role).first()

    def add_role_to_user(self, user, role):
        rv = super(MongoEngineUserDatastore, self).add_role_to_user(user, role)
        if rv:
            self.put(user)
        return rv