// import Counter from './components/Counter';

//import Counter, { counterVar as Counter3 , counterVar2 } from './components/Counter';

import React from 'react'; //node_modules/react/index.js 설치되어있는 모듈 불러올때는 경로가 필요 없음
import {type Product} from '@/app/components/Counter';

import Counter, { counterVar as Counter3 , counterVar2 } from '@/app/components/Counter';

console.log('counterVar:', Counter3);

export default function Home() {
    return <Counter />;
}
