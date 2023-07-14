export const insertProduct = ({name, price}) => {
    // console.log('name',name, 'price', price);
    return db('products')
    .insert ({name, price})
    .returning(['id','name','price'])
    }
    
