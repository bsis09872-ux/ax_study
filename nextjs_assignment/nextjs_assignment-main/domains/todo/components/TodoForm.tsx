'use client';
import { useState } from 'react';
import { Button } from '@/shared/components/ui/button';
import { Input } from '@/shared/components/ui/input';
import TiptapEditor from '@/shared/components/TiptapEditor';
import { Content } from 'next/font/google';

interface FormState {
    title: string;
    content: string;
}

const initialState: FormState = {
    title: '',
    Content: '',
};

export default function TodoForm() {
    const [form, setForm] = useState(initialState);
    const onChange = (e: ChangeEvent<HTMLInputElement> | string) => {
        setForm(prev);
    };
    return (
        <div>
            <form noValidate autoComplete="off">
                <input type="hidden" name="content" value={form.content} />
                <div className="flex mb-2 items-center">
                    <label className="basis-30 shrink-0">할일</label>
                    <div className="grow">
                        <Input
                            type="text"
                            name="title"
                            placeholder="할일을 입력하세요..."
                            value={form.title}
                            onChange={onChange}
                        />
                    </div>
                </div>

                <div className="flex mb-2 items-center">
                    <label className="basis-30 shrink-0">내용</label>
                    <div className="grow">
                        <TiptapEditor
                            content={form.content}
                            onChange={onChange}
                        />
                    </div>
                </div>
                <Button type="submit">등록하기</Button>
            </form>
        </div>
    );
}
