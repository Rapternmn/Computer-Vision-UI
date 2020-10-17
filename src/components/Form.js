import React from 'react'

function Form({ setState, img_url }) {

    const [state_local, setStateLocal] = React.useState("")

    const handleSubmit = (e) => {
        // Set Image URL
        setState(state_local)

        // Clear Form Value
        setStateLocal("")

        // Prevent Refresh
        e.preventDefault();
    }

    const handleChange = (event) => {
        setStateLocal(event.target.value)
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input type="text" onChange={handleChange} 
                    className="todo-input"
                    value={state_local}
                    placeholder="Paste Image URL" />
                <button className="todo-button" type="submit">
                    <i className="fas fa-plus-square"></i>
                </button>
            </form>
        </div>
    )
}

export default Form
