'use client';

import { useRouter } from 'next/navigation';
import { useTransition } from 'react';
import { Button } from '@/shared/components/ui/button';
import { logoutAction } from '../actions/logout.action';

export default function SignOutButton() {
    const router = useRouter();
    const [isPending, startTransition] = useTransition();

    const onClick = async () => {
        startTransition(async () => {
            const result = await logoutAction();
            if (result.success) {
                router.push('/sign_in');
                router.refresh();
            } else {
                // 로그아웃 처리 실패
                alert(result.message ?? '로그아웃 처리 실패');
            }
            // 알아서 인식해서 작동함으로 버튼 상태관리 필요 없음
        });

        // setIsPending(true); //처리중에는 버튼을 비활성화 시키는 코드
        // const result = await logoutAction();
        // if (result.success) {
        //     router.push('/sign_in'); //기본적으로 csr로 실행됨 -> 페이지 새로고침 필요
        //     router.refresh();
        // } else {
        //     //로그아웃 처리 실패
        //     alert(result.message ?? '로그아웃 처리 실패');
        //     setIsPending(true); //버튼 다시 활성화
        // }
    };

    return (
        <Button variant="outline" disabled={isPending} onClick={onClick}>
            로그아웃
        </Button>
    );
}
