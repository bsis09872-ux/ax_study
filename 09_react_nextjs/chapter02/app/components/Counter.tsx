export const counterVar = { test1: 1000, test2: 2000 };

export const counterVar2 = 200;

export interface Product {
    id: number;
    name: string;
};

//const ProductType = type {...} 이런식으로 해도 위와 동일하게 가능

export default function Counter(): React.JSX.Element {
    return <div>Counter!</div>;
}
