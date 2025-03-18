import pytest

from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_create_user():
    user_model = get_user_model()
    user = user_model.objects.create_user(
        username="test_user", email="test_user@mail.ru"
    )
    assert user_model.objects.get(username=user.username)


@pytest.mark.django_db
def test_not_existent_user_exception():
    user_model = get_user_model()
    with pytest.raises(user_model.DoesNotExist) as exc:
        user_model.objects.get(id=777)

    assert exc.type is user_model.DoesNotExist
