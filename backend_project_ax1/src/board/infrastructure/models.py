"""
메모
board table -> 게시판 설정
레코드 한 개 = 게시판 한 개

BOARD(ID) 1:N POSTS(ID-> 증감번호)

시간대 기준 UTC+0 - 영국 그리니치천문대 기준
한국 시간은 UTC+9

게시판 theme 설정은 게시판 테이블에 컬럼으로 추가할 수 있음 (여기서는 제외)

권한 설정 - 읽기(전체), 쓰기(회원), 보기(전체), 댓글(회원) 등 가능
"""
from datetime import datetime, timezone
from sqlalchemy import String, Text, Integer, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from shared.core.models import Base


class Board(Base):
    __tablename__ = "boards"

    id: Mapped[str] = mapped_column(String(40), primary_key=True)
    name: Mapped[str] = mapped_column(String(65), nullable=False)
    write_role: Mapped[str] = mapped_column(String(30), default="ALL", nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now(timezone.utc), nullable=False)

    modified_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True,
        onupdate=datetime.now(timezone.utc)
    )

    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)