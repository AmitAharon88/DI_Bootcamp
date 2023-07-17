const Planets = ({planets}) => {
    return (
        <ul class="list-group d-inline-block">
            {planets.map((planet) =>
                <li class="list-group-item" key={planet}>{planet}</li>
            )}
        </ul>
    )
};

export default Planets