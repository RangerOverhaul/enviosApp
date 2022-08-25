class SspRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read ssp models go to dbase_ssp
        """
        if model._meta.app_label == 'ssp':
            return 'dbase_ssp'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write ssp models go to dbase_ssp.
        """
        if model._meta.app_label == 'ssp':
            return 'dbase_ssp'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the ssp app is involved.
        """
        if obj1._meta.app_label == 'ssp' or \
           obj2._meta.app_label == 'ssp':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the ssp app only appears in the 'dbase_ssp'
        database.
        """
        if app_label == 'ssp':
            return db == 'dbase_ssp'
        return None
