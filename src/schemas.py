from pydantic import BaseModel, Field, ConfigDict
from typing import Annotated, Literal

class UserInput(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    senior_citizen: Annotated[Literal['Yes','No'],Field(alias="Senior Citizen",description='Whether the customer is a senior citizen',examples=['Yes','No'])]
    partner: Annotated[Literal['Yes','No'],Field(alias="Partner",description='Whether the customer has a partner',examples=['Yes','No'])]
    dependents: Annotated[Literal['Yes','No'],Field(alias="Dependents",description='Whether the customer has dependents',examples=['Yes','No'])]
    tenure_months: Annotated[int,Field(alias="Tenure Months",ge=0,description='Number of months the customer has stayed with the company')]
    internet_service: Annotated[Literal['Fibre optic','DSL','No'],Field(alias="Internet Service",description='Type of internet service',examples=['Fibre optic','DSL','No'])]
    online_security: Annotated[Literal['Yes','No'],Field(alias="Online Security",description='Whether online security service is enabled',examples=['Yes','No'])]
    online_backup: Annotated[Literal['Yes','No'],Field(alias="Online Backup",description='Whether online backup is enabled',examples=['Yes','No'])]
    device_protection: Annotated[Literal['Yes','No'],Field(alias="Device Protection",description='Whether device protection service is enabled',examples=['Yes','No'])]
    tech_support : Annotated[Literal['Yes','No'],Field(alias="Tech Support",description='Whether tech support service is enabled',examples=['Yes','No'])]
    contract: Annotated[Literal['Month-to-month','One year','Two year'],Field(alias="Contract",description='Type of customer contract',examples=['Month-to-month','One year','Two year'])]
    paperless_billing: Annotated[Literal['Yes','No'],Field(alias="Paperless Billing",description='Whether the customer uses paperless billing',examples=['Yes','No'])]
    payment_method: Annotated[Literal['Electronic check','Mailed check','Bank transfer (automatic)','Credit card (automatic)'],Field(alias="Payment Method",description='Customer payment method',examples=['Electronic check','Mailed check','Bank transfer (automatic)','Credit card (automatic)'])]
    monthly_charges: Annotated[float,Field(alias="Monthly Charges",ge=0,description='Customer monthly charges')]
    total_charges: Annotated[float,Field(alias="Total Charges",ge=0,description='Customer total charges')]


class PredictionResponse(BaseModel):
    prediction: Literal["Churn", "No Churn"]
    churn_probability: float