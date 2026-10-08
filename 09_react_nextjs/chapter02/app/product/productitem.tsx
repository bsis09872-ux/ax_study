import Badge from './Badge';

interface Product {
    itemName: string;
    itemPrice: number;
}

export default function ProductItem(props: Product): React.JSX.Element {
    //props.itemName = '갤럭시S 26';
    const { itemName, itemPrice } = props;
    return (
        <>
            <dl>
                <dt>상품명</dt>
                <dd>
                    <Badge theme="dark">할인상품</Badge>
                    {itemName}
                </dd>
            </dl>
            <dl>
                <dt>판매가</dt>
                <dd>{itemPrice}</dd>
            </dl>
        </>
    );
}
