import React from 'react';

export default function MemberLayout({
    children,
}: LayoutProps<'/member'>): React.ReactNode {
    return (
        <div>
            <h1>회원공통</h1>
            {children}
        </div>
    );
}
