const BootstarpCard = ({image, name, description, buttonLabel, buttonUrl}) => {
    return (
        <div className="card m-5" style={{width: '30rem'}}>
            <img className="card-img-top" src={image} alt="Card image cap" />
            <div className="card-body">
                <h5 className="card-title">{name}</h5>
                <p className="card-text">{description}</p>
                <a href={buttonUrl} class="btn btn-primary">{buttonLabel}</a>
            </div>
        </div>
    )
};

export default BootstarpCard