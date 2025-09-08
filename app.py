import streamlit as st

def generate_arithmetic_sequence(first_term, common_difference, num_terms):
    """
    Generate an arithmetic sequence based on the given parameters.
    
    Args:
        first_term (float): The first term of the sequence
        common_difference (float): The common difference between consecutive terms
        num_terms (int): The number of terms to generate
        
    Returns:
        list: A list containing the arithmetic sequence
    """
    sequence = []
    for n in range(num_terms):
        term = first_term + (n * common_difference)
        sequence.append(term)
    return sequence

def format_number(num):
    """
    Format a number for display, showing integers without decimal points.
    
    Args:
        num (float): The number to format
        
    Returns:
        str: Formatted number string
    """
    if num == int(num):
        return str(int(num))
    else:
        return f"{num:.2f}"

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Arithmetic Sequence Generator",
        page_icon="🔢",
        layout="centered"
    )
    
    # Main title and description
    st.title("🔢 Arithmetic Sequence Generator")
    st.markdown("Generate arithmetic sequences by specifying the first term, common difference, and number of terms.")
    
    # Create input columns for better layout
    col1, col2, col3 = st.columns(3)
    
    with col1:
        first_term = st.number_input(
            "First Term (a₁)",
            value=1.0,
            step=1.0,
            help="The first term of the arithmetic sequence"
        )
    
    with col2:
        common_difference = st.number_input(
            "Common Difference (d)",
            value=1.0,
            step=1.0,
            help="The constant difference between consecutive terms"
        )
    
    with col3:
        num_terms = st.number_input(
            "Number of Terms (n)",
            min_value=1,
            max_value=1000,
            value=10,
            step=1,
            help="How many terms to generate (between 1 and 1000)"
        )
    
    # Input validation
    if num_terms <= 0:
        st.error("⚠️ Number of terms must be a positive integer!")
        return
    
    if num_terms > 1000:
        st.error("⚠️ Number of terms cannot exceed 1000 for performance reasons!")
        return
    
    # Generate the sequence
    try:
        sequence = generate_arithmetic_sequence(first_term, common_difference, int(num_terms))
        
        # Display the mathematical formula
        st.subheader("📐 Formula")
        st.latex(r"a_n = a_1 + (n-1) \cdot d")
        
        # Show the specific formula with user values
        st.markdown(f"**Where:**")
        st.markdown(f"- a₁ (first term) = {format_number(first_term)}")
        st.markdown(f"- d (common difference) = {format_number(common_difference)}")
        st.markdown(f"- n (term number) = 1, 2, 3, ..., {int(num_terms)}")
        
        # Display the sequence
        st.subheader("📊 Generated Sequence")
        
        # Show sequence as a formatted list
        formatted_sequence = [format_number(term) for term in sequence]
        
        # Display in a nice format
        if len(sequence) <= 20:
            # For shorter sequences, display all terms in one line
            sequence_str = ", ".join(formatted_sequence)
            st.markdown(f"**Sequence:** {sequence_str}")
        else:
            # For longer sequences, display in multiple lines
            st.markdown("**Sequence:**")
            # Display first 10 terms
            first_part = ", ".join(formatted_sequence[:10])
            st.markdown(f"First 10 terms: {first_part}")
            
            # Display last 10 terms if sequence is long enough
            if len(sequence) > 20:
                last_part = ", ".join(formatted_sequence[-10:])
                st.markdown(f"Last 10 terms: {last_part}")
                st.markdown(f"... ({len(sequence) - 20} terms omitted)")
            else:
                remaining_part = ", ".join(formatted_sequence[10:])
                st.markdown(f"Remaining terms: {remaining_part}")
        
        # Display sequence statistics
        st.subheader("📈 Sequence Statistics")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("First Term", format_number(sequence[0]))
        
        with col2:
            st.metric("Last Term", format_number(sequence[-1]))
        
        with col3:
            if len(sequence) > 1:
                sequence_sum = sum(sequence)
                st.metric("Sum", format_number(sequence_sum))
            else:
                st.metric("Sum", format_number(sequence[0]))
        
        with col4:
            if len(sequence) > 1:
                avg = sum(sequence) / len(sequence)
                st.metric("Average", format_number(avg))
            else:
                st.metric("Average", format_number(sequence[0]))
        
        # Show expandable detailed view for longer sequences
        if len(sequence) > 20:
            with st.expander("View Complete Sequence"):
                # Display in chunks for better readability
                chunk_size = 10
                for i in range(0, len(sequence), chunk_size):
                    chunk = sequence[i:i + chunk_size]
                    formatted_chunk = [format_number(term) for term in chunk]
                    term_numbers = list(range(i + 1, min(i + chunk_size + 1, len(sequence) + 1)))
                    
                    st.markdown(f"**Terms {term_numbers[0]}-{term_numbers[-1]}:** {', '.join(formatted_chunk)}")
        
        # Educational note
        st.subheader("📚 About Arithmetic Sequences")
        st.markdown("""
        An **arithmetic sequence** is a sequence of numbers where the difference between 
        consecutive terms is constant. This difference is called the **common difference**.
        
        **Key Properties:**
        - Each term is found by adding the common difference to the previous term
        - The nth term formula: aₙ = a₁ + (n-1)d
        - The sum of n terms: Sₙ = n/2 × (2a₁ + (n-1)d)
        """)
        
    except Exception as e:
        st.error(f"⚠️ An error occurred while generating the sequence: {str(e)}")
        st.info("Please check your input values and try again.")

if __name__ == "__main__":
    main()
