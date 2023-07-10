import os

import pytest
from pytest_httpx import HTTPXMock

from lago_python_client.client import Client
from lago_python_client.exceptions import LagoApiError
from lago_python_client.models.plan_applied_tax import PlanAppliedTax


def applied_tax_object():
    return PlanAppliedTax(
        tax_code='tax_code'
    )


def mock_response():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(this_dir, 'fixtures/plan_applied_tax.json')

    with open(data_path, 'rb') as applied_tax_response:
        return applied_tax_response.read()


def test_valid_create_plan_applied_tax_request(httpx_mock: HTTPXMock):
    client = Client(api_key='886fe239-927d-4072-ab72-6dd345e8dd0d')
    plan_code = 'plan_code'

    httpx_mock.add_response(
        method='POST',
        url='https://api.getlago.com/api/v1/plans/' + plan_code + '/applied_taxes',
        content=mock_response()
    )
    response = client.plan_applied_taxes.create(plan_code, applied_tax_object())

    assert response.lago_id == 'b7ab2926-1de8-4428-9bcd-779314ac129b'
    assert response.tax_code == 'tax_code'


def test_invalid_create_plan_applied_tax_request(httpx_mock: HTTPXMock):
    client = Client(api_key='invalid')
    plan_code = 'plan_code'

    httpx_mock.add_response(
        method='POST',
        url='https://api.getlago.com/api/v1/plans/' + plan_code + '/applied_taxes',
        status_code=401,
        content=b''
    )

    with pytest.raises(LagoApiError):
        client.plan_applied_taxes.create(plan_code, applied_tax_object())


def test_valid_destroy_applied_tax_request(httpx_mock: HTTPXMock):
    client = Client(api_key='886fe239-927d-4072-ab72-6dd345e8dd0d')
    plan_code = 'plan_code'
    tax_code = 'tax_code'

    httpx_mock.add_response(
        method='DELETE',
        url='https://api.getlago.com/api/v1/plans/' + plan_code + '/applied_taxes/' + tax_code,
        content=mock_response()
    )
    response = client.plan_applied_taxes.destroy(plan_code, tax_code)

    assert response.plan_code == 'plan_code'
    assert response.tax_code == 'tax_code'


def test_invalid_destroy_applied_tax_request(httpx_mock: HTTPXMock):
    client = Client(api_key='invalid')
    plan_code = 'plan_code'
    tax_code = 'invalid'

    httpx_mock.add_response(
        method='DELETE',
        url='https://api.getlago.com/api/v1/plans/' + plan_code + '/applied_taxes/' + tax_code,
        status_code=404,
        content=b''
    )

    with pytest.raises(LagoApiError):
        client.plan_applied_taxes.destroy(plan_code, tax_code)
