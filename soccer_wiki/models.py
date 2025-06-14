from django.db import models


class SoccerWikiPlayer(models.Model):
    STATUS_UNKNOWN = 1
    STATUS_SUCCESS = 2
    STATUS_ERROR = 3

    STATUSES = (
        (STATUS_UNKNOWN, 'Unknown'),
        (STATUS_SUCCESS, 'Success'),
        (STATUS_ERROR, 'Error'),
    )

    import_id = models.IntegerField(unique=True)
    first_name = models.TextField(null=True)
    second_name = models.TextField(null=True)
    birth_date = models.DateField(null=True, db_index=True)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    image = models.TextField(null=True)
    internal_image_status = models.IntegerField(choices=STATUSES, default=STATUS_UNKNOWN)
    internal_image_url = models.TextField(null=True)

    def __str__(self):
        return "[{}] - {} {}".format(self.import_id, self.first_name, self.second_name)

    class Meta:
        db_table = 'soccer_wiki_players'
