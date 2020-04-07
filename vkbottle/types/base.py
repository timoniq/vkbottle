import pydantic
from vkbottle.framework.framework.extensions import dispatch


class BaseModel(pydantic.BaseModel):
    class Config:
        allow_mutation = False
        use_enum_values = True

    def __str__(self):
        return str(self.dict(skip_defaults=True))

    def __repr__(self):
        args = ", ".join(
            [f"{key}={value}" for key, value in self.dict(skip_defaults=True).items()]
        )
        return "{}({})".format(self.__class__.__name__, args)

    @staticmethod
    def get_params(params: dict) -> dict:
        return {
            k: dispatch(v)
            for k, v in params.items()
            if k != "self" and not k.startswith("_") and v is not None
        }
