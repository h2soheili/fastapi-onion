from fastapi import Depends, APIRouter, HTTPException

from core.service_app.configs.Logger import get_logger_gn
from core.service_app.configs.Settings import get_settings_gn, Settings

router = APIRouter(prefix='/v1')


@router.get('/config', description="get server configs", response_model=Settings)
async def get_server_config(settings=Depends(get_settings_gn, use_cache=True)):
    return settings.model_dump()


@router.patch('/config', description="update some config", response_model=Settings)
async def update_server_config(data: Settings,
                               settings=Depends(get_settings_gn, use_cache=True),
                               logger=Depends(get_logger_gn(__name__), use_cache=True)):
    try:
        for k, v in data.model_dump().items():
            setattr(settings, k, v)
        return settings.model_dump(mode='json')
    except Exception as e:
        logger.error("update_server_config error", e=e)
        raise HTTPException(detail=str(e), status_code=500)
