from typing import List, Optional

from lago_python_client.base_model import BaseModel

from ..base_model import BaseResponseModel
from .plan import PlanOverrides, PlanResponse


class Subscription(BaseModel):
    plan_code: Optional[str]
    external_customer_id: Optional[str]
    name: Optional[str]
    external_id: Optional[str]
    subscription_date: Optional[str]
    billing_time: Optional[str]
    ending_at: Optional[str]
    plan_overrides: Optional[PlanOverrides]


class SubscriptionResponse(BaseResponseModel):
    lago_id: str
    lago_customer_id: Optional[str]
    external_customer_id: Optional[str]
    canceled_at: Optional[str]
    created_at: Optional[str]
    plan_code: Optional[str]
    started_at: Optional[str]
    status: Optional[str]
    name: Optional[str]
    external_id: Optional[str]
    billing_time: Optional[str]
    terminated_at: Optional[str]
    ending_at: Optional[str]
    subscription_date: Optional[str]
    previous_plan_code: Optional[str]
    next_plan_code: Optional[str]
    downgrade_plan_date: Optional[str]
    plan: Optional[PlanResponse]


class SubscriptionsResponse(BaseResponseModel):
    __root__: List[SubscriptionResponse]
