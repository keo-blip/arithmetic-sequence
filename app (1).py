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

def generate_geometric_sequence(first_term, common_ratio, num_terms):
    """
    Generate a geometric sequence based on the given parameters.
    
    Args:
        first_term (float): The first term of the sequence
        common_ratio (float): The common ratio between consecutive terms
        num_terms (int): The number of terms to generate
        
    Returns:
        list: A list containing the geometric sequence
    """
    sequence = []
    for n in range(num_terms):
        term = first_term * (common_ratio ** n)
        sequence.append(term)
    return sequence

def calculate_geometric_sum(first_term, common_ratio, num_terms):
    """
    Calculate the sum of a finite geometric series.
    
    Args:
        first_term (float): The first term of the series
        common_ratio (float): The common ratio
        num_terms (int): The number of terms
        
    Returns:
        float: The sum of the geometric series
    """
    if common_ratio == 1:
        return first_term * num_terms
    else:
        return first_term * (1 - common_ratio**num_terms) / (1 - common_ratio)

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
        page_title="Mathematical Sequence Generator",
        page_icon="🔢",
        layout="centered"
    )
    
    # Main title and description
    st.title("🔢 Mathematical Sequence Generator")
    st.markdown("Generate arithmetic or geometric sequences with detailed analysis and calculations.")
    
    # Sequence type selection
    sequence_type = st.radio(
        "Choose Sequence Type:",
        ["Arithmetic Sequence", "Geometric Sequence"],
        horizontal=True,
        help="Select the type of mathematical sequence to generate"
    )
    
    # Create input columns for better layout
    col1, col2, col3 = st.columns(3)
    
    with col1:
        first_term = st.number_input(
            "First Term (a₁)",
            value=1.0,
            step=1.0,
            help="The first term of the sequence"
        )
    
    with col2:
        if sequence_type == "Arithmetic Sequence":
            second_param = st.number_input(
                "Common Difference (d)",
                value=1.0,
                step=1.0,
                help="The constant difference between consecutive terms"
            )
        else:  # Geometric Sequence
            second_param = st.number_input(
                "Common Ratio (r)",
                value=2.0,
                step=0.1,
                help="The constant ratio between consecutive terms"
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
    
    # Generate the sequence based on type
    try:
        if sequence_type == "Arithmetic Sequence":
            sequence = generate_arithmetic_sequence(first_term, second_param, int(num_terms))
            series_sum = sum(sequence)  # Simple sum for arithmetic
            
            # Display the mathematical formula
            st.subheader("📐 Formula")
            st.latex(r"a_n = a_1 + (n-1) \cdot d")
            
            # Show the specific formula with user values
            st.markdown(f"**Where:**")
            st.markdown(f"- a₁ (first term) = {format_number(first_term)}")
            st.markdown(f"- d (common difference) = {format_number(second_param)}")
            st.markdown(f"- n (term number) = 1, 2, 3, ..., {int(num_terms)}")
            
        else:  # Geometric Sequence
            sequence = generate_geometric_sequence(first_term, second_param, int(num_terms))
            series_sum = calculate_geometric_sum(first_term, second_param, int(num_terms))
            
            # Display the mathematical formula
            st.subheader("📐 Formula")
            st.latex(r"a_n = a_1 \cdot r^{(n-1)}")
            
            # Show the specific formula with user values
            st.markdown(f"**Where:**")
            st.markdown(f"- a₁ (first term) = {format_number(first_term)}")
            st.markdown(f"- r (common ratio) = {format_number(second_param)}")
            st.markdown(f"- n (term number) = 1, 2, 3, ..., {int(num_terms)}")
            
            # Show geometric series sum formula
            st.subheader("📊 Series Sum Formula")
            if second_param == 1:
                st.latex(r"S_n = n \cdot a_1")
                st.markdown(f"Since r = 1, the sum is simply: {int(num_terms)} × {format_number(first_term)} = {format_number(series_sum)}")
            else:
                st.latex(r"S_n = a_1 \cdot \frac{1 - r^n}{1 - r}")
                st.markdown(f"**Sum calculation:** {format_number(first_term)} × (1 - {format_number(second_param)}^{int(num_terms)}) / (1 - {format_number(second_param)}) = {format_number(series_sum)}")
        
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
            st.metric("Series Sum", format_number(series_sum))
        
        with col4:
            if len(sequence) > 1:
                avg = series_sum / len(sequence)
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
        if sequence_type == "Arithmetic Sequence":
            st.subheader("📚 About Arithmetic Sequences")
            st.markdown("""
            An **arithmetic sequence** is a sequence of numbers where the difference between 
            consecutive terms is constant. This difference is called the **common difference**.
            
            **Key Properties:**
            - Each term is found by adding the common difference to the previous term
            - The nth term formula: aₙ = a₁ + (n-1)d
            - The sum of n terms: Sₙ = n/2 × (2a₁ + (n-1)d)
            """)
        else:
            st.subheader("📚 About Geometric Sequences")
            st.markdown("""
            A **geometric sequence** is a sequence of numbers where each term after the first 
            is found by multiplying the previous term by a fixed, non-zero number called the **common ratio**.
            
            **Key Properties:**
            - Each term is found by multiplying the previous term by the common ratio
            - The nth term formula: aₙ = a₁ × r^(n-1)
            - The sum of n terms: Sₙ = a₁ × (1 - r^n) / (1 - r) when r ≠ 1
            - When r = 1: Sₙ = n × a₁
            - **Infinite series**: If |r| < 1, the infinite sum converges to a₁ / (1 - r)
            """)
            
            # Show infinite series calculation if applicable
            if abs(second_param) < 1 and second_param != 0:
                infinite_sum = first_term / (1 - second_param)
                st.info(f"💡 **Infinite Series Insight:** Since |r| = {abs(second_param):.3f} < 1, the infinite geometric series converges to: {format_number(infinite_sum)}")
        
    except Exception as e:
        st.error(f"⚠️ An error occurred while generating the sequence: {str(e)}")
        st.info("Please check your input values and try again.")

if __name__ == "__main__":
    main()
