import { type Todo } from '@/app/todo/page'; //타입으로 정의한 모듈은 type 명시하기 (권장)
import { FaCheckCircle, FaRegCheckCircle, FaRegTrashAlt } from 'react-icons/fa';

type TodoItemProps = Todo & {
    onClick: (id?: number) => void;
};

export default function TodoItem({
    id,
    title,
    checked,
    onClick,
}: TodoItemProps): React.JSX.Element {
    // const {id, title, checked} = item; -> TodoItem(item: Todo)이렇게 해도 됨.
    return (
        <li className="flex">
            <div className="flex" onClick={() => onClick(id)}>
                {checked ? <FaCheckCircle /> : <FaRegCheckCircle />}
                {title}
            </div>
            <span onClick={() => onRemove(id)}>
                <FaRegTrashAlt onClick={onRemove} />
            </span>
        </li>
    );
}
