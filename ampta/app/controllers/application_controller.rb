class ApplicationController < ActionController::Base
  protect_from_forgery
  before_filter :confirm_logged_in, :except => [:logout, :login, :do_login]
  before_filter :headernav

  def confirm_logged_in
    unless session[:user_id]
      flash[:notice] = "You must be logged in."
      redirect_to login_path
      return false
    else
      return true
    end
  end

  def login
    unless user_logged_in
      @user = User.new
      render :layout => 'login_page'
    else
      #redirect_to home_path
      render "index"
    end
  end

  def logout
    session[:user_id] = nil
    session[:user_name] = nil
    redirect_to login_path
  end

  def user_logged_in
    session[:user_id]
  end

  def headernav
    @user_name = session[:user_name]
  end
  
  def sidenav
    if user_logged_in
      # get logged in user
      @user = User.find(self.user_logged_in)
      # get projects and tickets for logged in user
      @projects_nav = @user.projects.order("id DESC")
      @tickets_nav = @user.tickets.order("id DESC").all(:limit => 10)
    end
  end

  def do_login
    user = User.authenticate(params[:user][:email], params[:user][:password])

    respond_to do |format|
      if user
        session[:user_id] = user.id
        session[:user_name] = "#{user.first_name} #{user.last_name}"
        format.html { redirect_to home_path, :notice => "Hello #{user.first_name}, thanks for logging in." }
      else
        format.html { redirect_to login_path, :notice => "That did not work." }
      end
    end
  end

end
