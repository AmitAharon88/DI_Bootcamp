const FormComponent = ({formInputs, handelSubmit}) => {
    console.log(formInputs)
    // handelSubmit
    return (
        <>
            <h1>Entered information</h1>
            <p>Your name: {formInputs.firstName} {formInputs.lastName} </p>
            <p>Your age: {formInputs.age} </p>
            <p>Your destination: {formInputs.destination} </p>
            <p>Your dietary restrictions:</p>
            <p>**Nuts free: {formInputs.nutsFree ? "Yes" : "No"}</p>
            <p>**Lactose free: {formInputs.lacFree ? "Yes" : "No"}</p>
            <p>**Vegan free: {formInputs.veganFree ? "Yes" : "No"}</p>
        </>
    );
};

export default FormComponent;