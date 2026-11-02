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
from sqlalchemy import String, Text, BigInteger, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from shared.core.models import Base


class Board(Base):
    """
    게시판 설정 테이블
    """
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

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }

class Post(Base):
    __tablename__="posts"

    id: Mapped[int] = mapped_column(
        BigInteger, 
        primary_key=True, 
        autoincrement=True
    )

    category: Mapped[str] = mapped_column(
        String(60),
        nullable=True,
        index=True
    )
    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now(timezone.utc), nullable=False)
    
    modified_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True,
        onupdate=datetime.now(timezone.utc)
    )

    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True) 

    # 날짜와 시간 같이 공통적인 부분은 상속 구조로 하는게 더 효율적이지 않을까? -> 연구해보기

    # 외래키
    # 관계 설정 N쪽이 자식쪽이라 보면 됨. 따라서 게시판 설정과 게시글 중에 게시글 쪽이 외래키가 들어가고 자식 테이블이 됨.
    # 참조 무결성 제약조건 - 자식이 있으면 부모를 삭제할 수 없음. 따라서 게시판 설정을 삭제하려면 게시글을 먼저 삭제해야 함.(Restrict)
    # ondelete="CASCADE" 옵션을 주면 부모가 삭제되면 자식도 삭제됨. 따라서 게시판 설정을 삭제하면 게시글도 같이 삭제됨.
    
    board_id: Mapped[str] = mapped_column(
        ForeignKey("boards.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    # 게시판 설정 (N:1)
    board_config: Mapped["Board"] = relationship()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
        }