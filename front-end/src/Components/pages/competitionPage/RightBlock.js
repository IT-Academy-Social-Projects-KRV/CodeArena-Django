import React from 'react';
import { Card } from 'react-bootstrap';
import { Component } from 'react';

class RightBlock extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        const { card } = this.props
        return (
            <>
                <Card bg="light" style={{ width: '15rem' }} >
                    <Card.Body style={{ height: '17rem' }}>
                        <Card.Img variant="top" style={{ height: '10rem' }} src={card.src} />
                        <Card.Text className="text-center m-3" >
                            <h5> {card.company_name} </h5>  
                        </Card.Text>
                    </Card.Body>
                </Card>
            </>
        )
    }
}

export default RightBlock