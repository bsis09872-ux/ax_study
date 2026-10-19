import { Button } from '@/shared/components/ui/button';
import { Input } from '@/shared/components/ui/input';
import { Button } from '@/shared/components/ui/button';
import { INITIAL_ACTION_STATE } from '@/shared/types/action.types';
import { useState } from 'react';

interface FormType {
    email: string;
    password: string;
    passwordConfirm: string;
    name: string;
}

const initialForm: FormType = {
    email: '',
    password: '',
    passwordConfirm: '',
    name: '',
};

export default function SignInForm(): React.JSX.Element {
    const [state, formAction, isPending] = useActionState(
        signUpAction,
        INITIAL_ACTION_STATE,
    );

    const [form, setForm] = useState(initialForm);

    const onChange = (e: ChangeEvent<HTMLInputElement>) => {
        setForm((prev) => ({ ...prev, [e.target.name]: e.target.value }));
    };
    return (
        <form method="post" noValidate autoComplete="off">
            <div className="mb-2">
                <Input type="email" name="email" placeholder="이메일" />
            </div>
            <div className="mb-2">
                <Input type="password" name="password" placeholder="비밀번호" />
            </div>
            <Button type="submit">로그인</Button>
        </form>
    );
}
