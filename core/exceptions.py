from django.http import Http404
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    if isinstance(exc, serializers.ValidationError):
        return Response({
            'code': 99999,
            'message': 'Validation error',
            'detail': exc.detail,
        }, status=exc.status_code)

    if isinstance(exc, Http404):
        exc = ObjectNotFound()

    # custom exception
    if isinstance(exc, CustomException):
        return Response({
            'code': exc.code,
            'message': exc.message
        }, status=exc.status_code)

    # fallback to default handler
    return exception_handler(exc, context)


class CustomException(Exception):
    code = 99999
    status_code = 400
    message = 'Unknown error'


class ObjectNotFound(CustomException):
    message = 'Not found'


class CannotUploadAvatar(CustomException):
    message = 'Upload avatar error'


class MatchIsNotAvailable(CustomException):
    message = 'Match is not available'


class InvalidNumberOfPicks(CustomException):
    message = 'Invalid number of picks'


class PickAlreadyEnded(CustomException):
    message = 'Pick already ended'


class YouAlreadyPickedThisPlayer(CustomException):
    message = 'You already picked this player'


class InvalidPowerUpPosition(CustomException):
    message = 'Invalid power-up position'


class InvalidMatchStatusForPowerUp(CustomException):
    message = 'You can apply power-ups when match is active'


class AlreadyActivePowerUpForPosition(CustomException):
    message = 'You already have active power-up for this position'


class NotEnoughBalanceForWithdraw(CustomException):
    message = 'Sorry, you need a minimum balance of $20 to cashout. Win some more games!'
