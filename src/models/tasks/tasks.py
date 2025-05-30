import datetime

from src.models.tasks.tasks_statemet import Statement
from src.models.tests.examples import Example
from src.models.tests.private_tests import PrivateTest

from pydantic import BaseModel, UUID4
from typing import List, Optional


class Tasks(BaseModel):
    id: UUID4
    title: str # Заголовок для задачи
    input_format_description: str  # Описание входных данных для задачи
    output_format_description: str # Описание выходных данных для задачи
    examples: List[Example]
    private_tests = List[PrivateTest]

    statement: Statement
    created_by: str # юз

    created_at: datetime
    updated_at: Optional[datetime] = datetime